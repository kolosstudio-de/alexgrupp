// Paste the new Sheet ID here after running setupSpreadsheet():
const SPREADSHEET_ID = '1fc0G4R1-4wPqW5Yblogz5ENbttQAiN8RX33wPqmxYbY';

const OWNER_EMAIL = 'info@oleksandrhalushka.de';
const CALENDAR_ID = 'primary'; 
const SHEET_ZAYAVKI_AUTO = 'Zayavki_Auto';
const SHEET_ZAYAVKI_BAU = 'Zayavki_Bau';
const SHEET_CLIENTS = 'Clients_All';
const SHEET_DASHBOARD = 'Dashboard';

function getSpreadsheetId() {
  const id = SPREADSHEET_ID || PropertiesService.getScriptProperties().getProperty('SPREADSHEET_ID');
  if (!id) throw new Error('SPREADSHEET_ID not set. Run setupSpreadsheet() first from the Script Editor.');
  return id;
}

function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('CRM Oleksandr Halushka')
    .addItem('1. Первоначальная настройка', 'setupSpreadsheet')
    .addItem('2. Применить красивый дизайн', 'setupCRMDesign')
    .addItem('3. Сгенерировать Дашборд (Аналитику)', 'setupAnalyticsDashboard')
    .addToUi();
}

function setupSpreadsheet() {
  const existing = PropertiesService.getScriptProperties().getProperty('SPREADSHEET_ID');
  if (existing && existing !== SPREADSHEET_ID) {
    const msg = 'Spreadsheet already exists! ID: ' + existing;
    console.log(msg);
  }
  
  const ss = SpreadsheetApp.openById(getSpreadsheetId());
  ensureSheets(ss);

  try { SpreadsheetApp.getUi().alert('CRM Создана!\nЗапустите теперь "Применить красивый дизайн" в меню CRM.'); } catch(e){}
  return getSpreadsheetId();
}

function ensureSheets(ss) {
  const zH = ['ID Заявки','Дата создания','Имя','Фамилия','Email','Телефон','Тип клиента','Язык','Услуга (Тема)','Сообщение (от клиента)','Детали (Авто/Объект)','Статус','Причина отказа','Дата в Календаре','UTM Источник','Выручка (€)','Расход (€)','Заметки','EventId'];
  const cH = ['ClientID','Имя','Фамилия','Email','Телефон','Тип клиента','Адрес / Город','День рождения','Источник (UTM)','Первое обращение','Последний визит','Кол-во обращений','Общая выручка (€)','Средний чек (€)','Сегмент (ABC)'];
  
  if (!ss.getSheetByName(SHEET_ZAYAVKI_AUTO)) { ss.insertSheet(SHEET_ZAYAVKI_AUTO).appendRow(zH); }
  if (!ss.getSheetByName(SHEET_ZAYAVKI_BAU)) { ss.insertSheet(SHEET_ZAYAVKI_BAU).appendRow(zH); }
  if (!ss.getSheetByName(SHEET_CLIENTS)) { ss.insertSheet(SHEET_CLIENTS).appendRow(cH); }
}

function setupCRMDesign() {
  const ss = SpreadsheetApp.openById(getSpreadsheetId());
  
  const zH = ['ID Заявки','Дата создания','Имя','Фамилия','Email','Телефон','Тип клиента','Язык','Услуга (Тема)','Сообщение (от клиента)','Детали (Авто/Объект)','Статус','Причина отказа','Дата в Календаре','UTM Источник','Выручка (€)','Расход (€)','Заметки','EventId'];
  
  [SHEET_ZAYAVKI_AUTO, SHEET_ZAYAVKI_BAU].forEach(sheetName => {
    const sheet = ss.getSheetByName(sheetName);
    if (!sheet) return;
    
    // Clear and set headers
    sheet.clear();
    sheet.appendRow(zH);
    
    // Freeze top row
    sheet.setFrozenRows(1);
    
    // Header styling
    const headerRange = sheet.getRange(1, 1, 1, zH.length);
    headerRange.setBackground('#0f172a').setFontColor('white').setFontWeight('bold').setHorizontalAlignment('center');
    
    // Dropdowns
    const ruleStatus = SpreadsheetApp.newDataValidation().requireValueInList(['Новая', 'В работе', 'Подтверждена', 'Завершена', 'Отменена'], true).build();
    sheet.getRange(2, 12, 999).setDataValidation(ruleStatus); // Статус
    
    const ruleReason = SpreadsheetApp.newDataValidation().requireValueInList(['-', 'Дорого', 'Ушел к конкурентам', 'Не подошли сроки', 'Передумал', 'Спам'], true).build();
    sheet.getRange(2, 13, 999).setDataValidation(ruleReason); // Причина отказа
    
    const ruleB2B = SpreadsheetApp.newDataValidation().requireValueInList(['B2C (Частник)', 'B2B (Компания)'], true).build();
    sheet.getRange(2, 7, 999).setDataValidation(ruleB2B); // Тип клиента
    
    // Auto-resize and specific widths
    sheet.setColumnWidth(2, 150); // Date
    sheet.setColumnWidth(5, 200); // Email
    sheet.setColumnWidth(10, 300); // Message
  });
  
  const cH = ['ClientID','Имя','Фамилия','Email','Телефон','Тип клиента','Адрес / Город','День рождения','Источник (UTM)','Первое обращение','Последний визит','Кол-во обращений','Общая выручка (€)','Средний чек (€)','Сегмент (ABC)'];
  const clientSheet = ss.getSheetByName(SHEET_CLIENTS);
  if (clientSheet) {
    clientSheet.clear();
    clientSheet.appendRow(cH);
    clientSheet.setFrozenRows(1);
    clientSheet.getRange(1, 1, 1, cH.length).setBackground('#16a34a').setFontColor('white').setFontWeight('bold').setHorizontalAlignment('center');
    
    const ruleB2B = SpreadsheetApp.newDataValidation().requireValueInList(['B2C (Частник)', 'B2B (Компания)'], true).build();
    clientSheet.getRange(2, 6, 999).setDataValidation(ruleB2B);
    
    const ruleABC = SpreadsheetApp.newDataValidation().requireValueInList(['A (VIP)', 'B (Обычный)', 'C (Проблемный)', 'New'], true).build();
    clientSheet.getRange(2, 15, 999).setDataValidation(ruleABC);
  }
  
  // Clean up old sheets
  ['Лист1', 'Clients_Auto', 'Clients_Bau'].forEach(name => {
    const s = ss.getSheetByName(name);
    if (s) ss.deleteSheet(s);
  });
  
  try { SpreadsheetApp.getUi().alert('Дизайн и Архитектура успешно применены (v4)!'); } catch(e){}
}

function onEdit(e) {
  if (!e || !e.range) return;
  const sheet = e.range.getSheet();
  const sheetName = sheet.getName();
  
  if (sheetName !== SHEET_ZAYAVKI_AUTO && sheetName !== SHEET_ZAYAVKI_BAU) return;
  
  const col = e.range.getColumn();
  const row = e.range.getRow();
  
  if (col === 12 || col === 14) {
    const status = sheet.getRange(row, 12).getValue();
    const calendarDate = sheet.getRange(row, 14).getValue();
    const existingEventId = sheet.getRange(row, 19).getValue();
    
    if (status === 'Подтверждена') {
      if (!calendarDate) {
        if (col === 12) SpreadsheetApp.getUi().alert('Внимание: Вы выбрали статус "Подтверждена", но не указали дату (Колонка N). Встреча не создана.');
        return;
      }
      
      const eventId = createOrUpdateCalendarEvent(sheet, row, sheetName);
      if (eventId) {
        sheet.getRange(row, 19).setValue(eventId);
        if (col === 12 && !existingEventId) {
          SpreadsheetApp.getUi().alert('Успех: Событие создано в Google Календаре!');
          sendFinalConfirmationEmail(sheet, row, sheetName, calendarDate);
        } else if (col === 14 && existingEventId) {
          SpreadsheetApp.getUi().alert('Успех: Событие в Google Календаре обновлено на новую дату!');
        }
      }
    } else if (status === 'Отменена' && existingEventId) {
      try {
        const cal = CalendarApp.getCalendarById(CALENDAR_ID);
        const event = cal.getEventById(existingEventId);
        if (event) event.deleteEvent();
        SpreadsheetApp.getUi().alert('Встреча удалена из Google Календаря.');
      } catch(err) { console.warn('Could not delete event: ' + err); }
      sheet.getRange(row, 19).setValue('');
    }
  }
}

function clearAllData() {
  const ss = SpreadsheetApp.openById(getSpreadsheetId());
  const sheets = [SHEET_ZAYAVKI_AUTO, SHEET_ZAYAVKI_BAU, SHEET_CLIENTS];
  
  sheets.forEach(name => {
    const sheet = ss.getSheetByName(name);
    if (sheet) {
      const lastRow = sheet.getLastRow();
      if (lastRow > 1) {
        sheet.getRange(2, 1, lastRow - 1, sheet.getLastColumn()).clearContent();
      }
    }
  });
}

function setupAnalyticsDashboard() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) return;
  
  let sheet = ss.getSheetByName(SHEET_DASHBOARD);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_DASHBOARD, 0);
  } else {
    sheet.clear();
  }
  
  sheet.setTabColor('#3b82f6');
  sheet.setHiddenGridlines(true);
  
  // Set Background
  sheet.getRange(1, 1, 50, 15).setBackground('#0f172a').setFontColor('#ffffff').setFontFamily('Arial');
  
  // Title
  sheet.getRange('B2').setValue('💼 БИЗНЕС АНАЛИТИКА (DASHBOARD)').setFontSize(24).setFontWeight('bold');
  sheet.getRange('B3').setValue('Автоматический сводный отчет по всем направлениям (Auto & Bau)').setFontSize(12).setFontColor('#94a3b8');
  
  const createMetric = (col, row, title, formula, color) => {
    sheet.getRange(row, col, 1, 2).merge().setValue(title).setFontSize(11).setFontColor('#94a3b8').setBackground('#1e293b').setBorder(true,true,false,true,false,false,'#334155',SpreadsheetApp.BorderStyle.SOLID_MEDIUM).setVerticalAlignment('middle');
    const valCell = sheet.getRange(row+1, col, 1, 2).merge().setFormula(formula).setFontSize(24).setFontWeight('bold').setFontColor(color).setBackground('#1e293b').setBorder(false,true,true,true,false,false,'#334155',SpreadsheetApp.BorderStyle.SOLID_MEDIUM).setVerticalAlignment('middle');
    return valCell;
  };
  
  sheet.setColumnWidth(2, 180);
  sheet.setColumnWidth(3, 180);
  sheet.setColumnWidth(4, 180);
  sheet.setColumnWidth(5, 180);
  sheet.setColumnWidth(6, 180);
  sheet.setColumnWidth(7, 180);
  sheet.setColumnWidth(8, 180);
  sheet.setColumnWidth(9, 180);

  // ROW 5, 6: KPI Cards
  createMetric(2, 5, 'ВСЕГО ЗАЯВОК', '=COUNTA(Zayavki_Auto!A2:A) + COUNTA(Zayavki_Bau!A2:A)', '#ffffff');
  createMetric(4, 5, 'ПОДТВЕРЖДЕНО', '=COUNTIF(Zayavki_Auto!L2:L, "Подтверждена") + COUNTIF(Zayavki_Bau!L2:L, "Подтверждена")', '#10b981');
  
  sheet.getRange(6, 6, 1, 2).setNumberFormat('0.0%');
  createMetric(6, 5, 'КОНВЕРСИЯ', '=IFERROR((COUNTIF(Zayavki_Auto!L2:L, "Подтверждена") + COUNTIF(Zayavki_Bau!L2:L, "Подтверждена")) / (COUNTA(Zayavki_Auto!A2:A) + COUNTA(Zayavki_Bau!A2:A)), 0)', '#3b82f6');
  
  sheet.getRange(6, 8, 1, 2).setNumberFormat('€#,##0.00');
  createMetric(8, 5, 'ОБЩАЯ ВЫРУЧКА', '=SUM(Zayavki_Auto!P2:P) + SUM(Zayavki_Bau!P2:P)', '#f59e0b');
  
  // ROW 8, 9: Financials
  sheet.getRange(9, 2, 1, 2).setNumberFormat('€#,##0.00');
  createMetric(2, 8, 'РАСХОДЫ (ЗАТРАТЫ)', '=SUM(Zayavki_Auto!Q2:Q) + SUM(Zayavki_Bau!Q2:Q)', '#ef4444');
  
  sheet.getRange(9, 4, 1, 2).setNumberFormat('€#,##0.00');
  createMetric(4, 8, 'ЧИСТАЯ ПРИБЫЛЬ', '=(SUM(Zayavki_Auto!P2:P) + SUM(Zayavki_Bau!P2:P)) - (SUM(Zayavki_Auto!Q2:Q) + SUM(Zayavki_Bau!Q2:Q))', '#10b981');

  sheet.getRange(9, 6, 1, 2).setNumberFormat('€#,##0.00');
  createMetric(6, 8, 'СРЕДНИЙ ЧЕК', '=IFERROR((SUM(Zayavki_Auto!P2:P) + SUM(Zayavki_Bau!P2:P)) / (COUNTIF(Zayavki_Auto!L2:L, "Подтверждена") + COUNTIF(Zayavki_Bau!L2:L, "Подтверждена")), 0)', '#a855f7');

  // Tables
  sheet.getRange('B11:E11').merge().setValue('РАСПРЕДЕЛЕНИЕ ПО НАПРАВЛЕНИЯМ').setFontSize(12).setFontWeight('bold');
  sheet.getRange('B12').setValue('Направление').setBackground('#334155');
  sheet.getRange('C12').setValue('Заявки').setBackground('#334155');
  sheet.getRange('D12').setValue('Успешно').setBackground('#334155');
  sheet.getRange('E12').setValue('Выручка').setBackground('#334155');
  
  sheet.getRange('B13').setValue('Auto (СТО)');
  sheet.getRange('C13').setFormula('=COUNTA(Zayavki_Auto!A2:A)');
  sheet.getRange('D13').setFormula('=COUNTIF(Zayavki_Auto!L2:L, "Подтверждена")');
  sheet.getRange('E13').setFormula('=SUM(Zayavki_Auto!P2:P)').setNumberFormat('€#,##0.00');
  
  sheet.getRange('B14').setValue('Bau (Ремонт)');
  sheet.getRange('C14').setFormula('=COUNTA(Zayavki_Bau!A2:A)');
  sheet.getRange('D14').setFormula('=COUNTIF(Zayavki_Bau!L2:L, "Подтверждена")');
  sheet.getRange('E14').setFormula('=SUM(Zayavki_Bau!P2:P)').setNumberFormat('€#,##0.00');
  
  sheet.getRange('G11:I11').merge().setValue('UTM ИСТОЧНИКИ').setFontSize(12).setFontWeight('bold');
  sheet.getRange('G12').setValue('Источник').setBackground('#334155');
  sheet.getRange('H12').setValue('Заявки').setBackground('#334155');
  sheet.getRange('I12').setValue('Выручка').setBackground('#334155');
  
  sheet.getRange('G13').setFormula(`=QUERY({Zayavki_Auto!O2:P; Zayavki_Bau!O2:P}, "select Col1, count(Col1), sum(Col2) where Col1 is not null group by Col1 order by sum(Col2) desc label Col1 '', count(Col1) '', sum(Col2) ''")`);
  sheet.getRange('I13:I30').setNumberFormat('€#,##0.00');
  
  SpreadsheetApp.getUi().alert('Дашборд успешно сгенерирован! Перейдите на лист "Dashboard".');
}

function createOrUpdateCalendarEvent(sheet, row, source) {
  try {
    const dataValues = sheet.getRange(row, 1, 1, 19).getValues()[0];
    const firstName = dataValues[2];
    const lastName = dataValues[3];
    const email = dataValues[4];
    const phone = dataValues[5];
    const topic = dataValues[8]; // Услуга (Тема) is 9th column (index 8)
    const calendarDate = dataValues[13]; // Дата в Календаре is 14th column (index 13)
    const notes = dataValues[17]; // Заметки is 18th column (index 17)
    const existingEventId = dataValues[18]; // EventId is 19th column (index 18)
    
    const cal = CalendarApp.getCalendarById(CALENDAR_ID);
    const start = new Date(calendarDate);
    const end = new Date(start.getTime() + 60 * 60 * 1000); 
    
    const title = 'CRM: ' + firstName + ' ' + lastName + ' (' + source + ')';
    const description = `Тема: ${topic}\nТелефон: ${phone}\nEmail: ${email}\nЗаметки: ${notes}`;
    const location = source === SHEET_ZAYAVKI_AUTO ? 'Industriestr. 22, 93077 Bad Abbach' : '';
    
    if (existingEventId) {
      try {
        const event = cal.getEventById(existingEventId);
        if (event) {
          event.setTime(start, end);
          event.setDescription(description);
          return existingEventId;
        }
      } catch (err) {
        console.warn("Could not find existing event to update, creating new one.", err);
      }
    }
    
    const newEvent = cal.createEvent(title, start, end, {
      description: description,
      location: location
    });
    if (source === SHEET_ZAYAVKI_BAU) newEvent.setColor(CalendarApp.EventColor.ORANGE);
    else newEvent.setColor(CalendarApp.EventColor.BLUE);
    
    return newEvent.getId();
  } catch (err) {
    console.error("Calendar create error: " + err);
    SpreadsheetApp.getUi().alert('Ошибка календаря: ' + err.message);
    return null;
  }
}

function doGet(e) {
  if (e && e.parameter && e.parameter.action === 'setup') {
    try {
      const sheetId = setupSpreadsheet();
      return ContentService.createTextOutput(JSON.stringify({ status: 'ok', spreadsheetId: sheetId }))
        .setMimeType(ContentService.MimeType.JSON);
    } catch(err) {
      return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
        .setMimeType(ContentService.MimeType.JSON);
    }
  }
  if (e && e.parameter && e.parameter.action === 'design') {
    try {
      setupCRMDesign();
      return ContentService.createTextOutput(JSON.stringify({ status: 'ok', message: 'Design applied (v4)' }))
        .setMimeType(ContentService.MimeType.JSON);
    } catch(err) {
      return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
        .setMimeType(ContentService.MimeType.JSON);
    }
  }
  if (e && e.parameter && e.parameter.action === 'clearAllData') {
    try {
      clearAllData();
      return ContentService.createTextOutput(JSON.stringify({ status: 'ok', message: 'All tables cleared.' }))
        .setMimeType(ContentService.MimeType.JSON);
    } catch(err) {
      return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
        .setMimeType(ContentService.MimeType.JSON);
    }
  }
  if (e && e.parameter && e.parameter.action === 'mobile_confirm') {
    const t = HtmlService.createTemplateFromFile('MobileConfirmUI');
    t.leadId = e.parameter.leadId || '';
    t.source = e.parameter.source || 'Auto';
    return t.evaluate().setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL).setTitle('Termin Bestätigen');
  }
  return ContentService.createTextOutput("Oleksandr Halushka CRM V8 Active");
}

function executeFinalConfirmation(leadId, finalTime, notes, status) {
  const ss = SpreadsheetApp.openById(getSpreadsheetId());
  const sheets = [ss.getSheetByName(SHEET_ZAYAVKI_AUTO), ss.getSheetByName(SHEET_ZAYAVKI_BAU)];
  
  for (const sheet of sheets) {
    if (!sheet) continue;
    const data = sheet.getDataRange().getValues();
    for (let r = 1; r < data.length; r++) {
      if (data[r][0] === leadId) { // Column 1: ID Заявки
        const row = r + 1;
        if (notes) sheet.getRange(row, 18).setValue(notes); // Заметки
        
        if (status === 'Confirmed') {
          sheet.getRange(row, 14).setValue(finalTime); // Дата в календаре
          sheet.getRange(row, 12).setValue('Подтверждена'); // Статус
          
          const eventId = createOrUpdateCalendarEvent(sheet, row, sheet.getName());
          if (eventId) {
            sheet.getRange(row, 19).setValue(eventId);
            sendFinalConfirmationEmail(sheet, row, sheet.getName(), finalTime);
          }
        } else if (status === 'Reject') {
          sheet.getRange(row, 12).setValue('Отменена');
          const existingEventId = sheet.getRange(row, 19).getValue();
          if (existingEventId) {
            try { CalendarApp.getCalendarById(CALENDAR_ID).getEventById(existingEventId).deleteEvent(); } catch(err) {}
            sheet.getRange(row, 19).setValue('');
          }
        }
        return 'success';
      }
    }
  }
  throw new Error("Заявка с ID " + leadId + " не найдена.");
}

function escapeHtml(value) {
  return String(value == null ? '' : value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function isLikelySpam(data) {
  if (data && typeof data.website === 'string' && data.website.trim() !== '') return 'honeypot';
  const fillMs = Number(data && data.fillTime);
  if (Number.isFinite(fillMs) && fillMs > 0 && fillMs < 3000) return 'too_fast';
  return null;
}

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const spamReason = isLikelySpam(data);
    if (spamReason) {
      return ContentService.createTextOutput(JSON.stringify({ status: 'success' })).setMimeType(ContentService.MimeType.JSON);
    }

    const ss = SpreadsheetApp.openById(getSpreadsheetId());
    ensureSheets(ss);
    const targetSheetName = data.source === 'Bau' ? SHEET_ZAYAVKI_BAU : SHEET_ZAYAVKI_AUTO;
    const sheet = ss.getSheetByName(targetSheetName);
    
    // ['ID Заявки','Дата создания','Имя','Фамилия','Email','Телефон','Тип клиента','Язык','Услуга (Тема)','Сообщение (от клиента)','Детали (Авто/Объект)','Статус','Причина отказа','Дата в Календаре','UTM Источник','Выручка (€)','Расход (€)','Заметки','EventId'];
    
    const leadId = "Z-" + Utilities.getUuid().substring(0,6).toUpperCase();
    
    let eventId = '';
    try {
      const cal = CalendarApp.getCalendarById(CALENDAR_ID);
      let startStr = data.prefDate;
      let startHour = 10;
      if (data.prefTime && data.prefTime !== 'any') {
        const parts = data.prefTime.split('-');
        if (parts.length > 0) {
          const timeParts = parts[0].split(':');
          if (timeParts.length > 0) startHour = parseInt(timeParts[0], 10);
        }
      }
      let startDate = new Date(startStr);
      if (isNaN(startDate.getTime())) startDate = new Date();
      startDate.setHours(startHour, 0, 0, 0);
      const endDate = new Date(startDate.getTime() + 60 * 60 * 1000);
      
      const title = '\\u260E\\uFE0F Заявка: ' + (data.firstName || '') + ' ' + (data.lastName || '') + ' (' + (data.source || 'Website') + ')';
      const description = `Тема: ${data.topic}\nТелефон: ${data.phone}\nEmail: ${data.email}\nСообщение: ${data.message}\nОжидание: ${data.prefTime}\nCRM ID: ${leadId}`;
      
      const newEvent = cal.createEvent(title, startDate, endDate, { description: description });
      newEvent.setColor(CalendarApp.EventColor.YELLOW);
      eventId = newEvent.getId();
    } catch(err) { console.warn("Could not create initial reminder event: " + err); }
    
    const rowData = [
      leadId,
      data.timestamp || new Date().toISOString(),
      data.firstName || "",
      data.lastName || "",
      data.email || "",
      data.phone || "",
      'B2C (Частник)', // Тип клиента (По умолчанию)
      data.language || "de",
      data.topic || "",
      data.message || "",
      '', // Детали (Авто/Объект)
      'Новая', // Статус
      '-', // Причина отказа
      '', // Дата в календаре
      data.utmSource || 'Website', // UTM Источник
      '', // Выручка
      '', // Расход
      '', // Заметки
      eventId // EventId
    ];
    
    sheet.appendRow(rowData);
    syncClient(data);
    try { sendOwnerNotification(data, sheet.getLastRow(), leadId); } catch(ignore) {}
    try { sendInitialConfirmation(data); } catch(ignore) {}
    
    return ContentService.createTextOutput(JSON.stringify({ status: 'success' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function syncClient(data) {
  const ss = SpreadsheetApp.openById(getSpreadsheetId());
  const sheet = ss.getSheetByName(SHEET_CLIENTS);
  if (!sheet) return;
  
  const rows = sheet.getDataRange().getValues();
  const email = (data.email || "").toLowerCase();
  const phone = data.phone || "";
  let foundIndex = -1;
  
  for (let i = 1; i < rows.length; i++) {
    if ((rows[i][3] && rows[i][3].toLowerCase() === email) || (rows[i][4] && rows[i][4] === phone)) {
      foundIndex = i + 1;
      break;
    }
  }
  
  if (foundIndex > 0) {
    const currentVisits = rows[foundIndex-1][11] || 0; // Кол-во обращений is col 12 (index 11)
    sheet.getRange(foundIndex, 11).setValue(new Date()); // LastVisit is col 11 (index 10)
    sheet.getRange(foundIndex, 12).setValue(currentVisits + 1); // Visits
  } else {
    // ['ClientID','Имя','Фамилия','Email','Телефон','Тип клиента','Адрес / Город','День рождения','Источник (UTM)','Первое обращение','Последний визит','Кол-во обращений','Общая выручка (€)','Средний чек (€)','Сегмент (ABC)'];
    sheet.appendRow(["C-" + Utilities.getUuid().substring(0,8), data.firstName, data.lastName, email, phone, 'B2C (Частник)', '', '', data.utmSource || 'Website', new Date(), new Date(), 1, 0, 0, 'New']);
  }
}

const topicDict = {
  de: {
    'inspektion': 'Inspektion & Wartung', 'reifenwechsel': 'Reifenwechsel & Bremsen', 'diagnose': 'Motordiagnose & Reparatur', 'tuning': 'Tuning & Zubehör', 'sonstiges-auto': 'Sonstiges (Auto)',
    'fliesen': 'Fliesenarbeiten', 'bodenverlegung': 'Bodenverlegung', 'naturstein': 'Naturstein & Terrassen', 'feinarbeiten': 'Montage & Feinarbeiten', 'sonstiges-bau': 'Sonstiges (Bau)'
  },
  uk: {
    'inspektion': 'Техогляд та обслуговування', 'reifenwechsel': 'Заміна шин та гальм', 'diagnose': 'Діагностика та ремонт', 'tuning': 'Тюнінг та аксесуари', 'sonstiges-auto': 'Інше (Авто)',
    'fliesen': 'Плиткові роботи', 'bodenverlegung': 'Укладання підлоги', 'naturstein': 'Природний камінь та тераси', 'feinarbeiten': 'Монтаж та чистові роботи', 'sonstiges-bau': 'Інше (Будівництво)'
  },
  ru: {
    'inspektion': 'Техосмотр и обслуживание', 'reifenwechsel': 'Шиномонтаж и тормоза', 'diagnose': 'Диагностика и ремонт', 'tuning': 'Тюнинг и аксессуары', 'sonstiges-auto': 'Другое (Авто)',
    'fliesen': 'Плиточные работы', 'bodenverlegung': 'Укладка пола', 'naturstein': 'Природный камень и террасы', 'feinarbeiten': 'Монтаж и чистовые работы', 'sonstiges-bau': 'Другое (Строительство)'
  },
  en: {
    'inspektion': 'Inspection & Maintenance', 'reifenwechsel': 'Tire Change & Brakes', 'diagnose': 'Engine Diagnostics & Repair', 'tuning': 'Tuning & Accessories', 'sonstiges-auto': 'Other (Auto)',
    'fliesen': 'Tiling Works', 'bodenverlegung': 'Flooring Installation', 'naturstein': 'Natural Stone & Terraces', 'feinarbeiten': 'Assembly & Finishing Works', 'sonstiges-bau': 'Other (Construction)'
  }
};

function getTranslatedTopic(topicKey, lang) {
  return (topicDict[lang] && topicDict[lang][topicKey]) || (topicDict['de'] && topicDict['de'][topicKey]) || topicKey;
}

function getSignatureHtml(type) {
  const auto = `<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;max-width:440px;width:100%;border:0;"><tr><td style="padding:10px 0;"><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:top;"><div style="font-size:20px;font-weight:800;color:#0f172a;letter-spacing:-0.4px;line-height:1.2;">Oleksandr Halushka</div><div style="font-size:10px;color:#3b7dd8;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-top:4px;">Kfz-Kaufberatung · Bayern</div><div style="font-size:9px;color:#94a3b8;margin-top:2px;">Einzelunternehmer</div></td><td style="vertical-align:top;text-align:right;width:34px;padding-left:10px;"><img src="https://files.catbox.moe/aln5jw.png" width="34" alt="OH Monogram Logo" style="display:inline-block;border:0;width:34px;height:auto;" /></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:12px;margin-bottom:12px;"><tr><td style="border-top:1px solid #cbd5e1;height:1px;"></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:top;width:290px;"><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Telefon</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="tel:+4916093409671" style="color:#0f172a;text-decoration:none;font-size:12px;font-weight:500;">+49 160 9340 9671</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">WhatsApp</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="https://wa.me/4916093409671" style="color:#3b7dd8;text-decoration:none;font-size:12px;font-weight:500;">Nachricht senden →</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">E-Mail</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="mailto:info@oleksandrhalushka.de" style="color:#0f172a;text-decoration:none;font-size:12px;font-weight:500;">info@oleksandrhalushka.de</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Adresse</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><span style="color:#334155;font-size:12px;">Industriestraße 22, 93077 Bad Abbach</span></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:0;font-size:9px;color:#94a3b8;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Instagram</td><td style="vertical-align:middle;padding-bottom:0;font-family:Arial,sans-serif;line-height:16px;"><a href="https://www.instagram.com/oleksandrhalushka.auto/" style="color:#3b7dd8;text-decoration:none;font-size:12px;">@oleksandrhalushka.auto</a></td></tr></table></td><td style="vertical-align:bottom;text-align:right;padding-left:10px;padding-bottom:2px;width:75px;"><img src="https://files.catbox.moe/05gl5o.png" height="42" alt="Handwritten Signature" style="display:inline-block;border:0;height:42px;width:auto;" /></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:12px;margin-bottom:8px;"><tr><td style="border-top:1px solid #cbd5e1;height:1px;"></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td><a href="https://www.oleksandrhalushka.de" style="color:#64748b;text-decoration:none;font-size:11px;">www.oleksandrhalushka.de</a></td><td style="text-align:right;"><a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color:#94a3b8;text-decoration:none;font-size:11px;">Impressum</a></td></tr></table></td></tr></table></td></tr></table>`;
  const bau = `<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;max-width:440px;width:100%;border:0;"><tr><td style="padding:10px 0;"><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:top;"><div style="font-size:20px;font-weight:800;color:#0f172a;letter-spacing:-0.4px;line-height:1.2;">Oleksandr Halushka</div><div style="font-size:10px;color:#d97706;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-top:4px;">Innenausbau &amp; Fliesenarbeiten · Bayern</div><div style="font-size:9px;color:#94a3b8;margin-top:2px;">Einzelunternehmer</div></td><td style="vertical-align:top;text-align:right;width:34px;padding-left:10px;"><img src="https://files.catbox.moe/x31v8f.png" width="34" alt="OH Monogram Logo" style="display:inline-block;border:0;width:34px;height:auto;" /></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:12px;margin-bottom:12px;"><tr><td style="border-top:1px solid #cbd5e1;height:1px;"></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:top;width:290px;"><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Telefon</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="tel:+4916093409671" style="color:#0f172a;text-decoration:none;font-size:12px;font-weight:500;">+49 160 9340 9671</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">WhatsApp</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="https://wa.me/4916093409671" style="color:#d97706;text-decoration:none;font-size:12px;font-weight:500;">Nachricht senden →</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">E-Mail</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="mailto:info@oleksandrhalushka.de" style="color:#0f172a;text-decoration:none;font-size:12px;font-weight:500;">info@oleksandrhalushka.de</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Adresse</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><span style="color:#334155;font-size:12px;">Industriestraße 22, 93077 Bad Abbach</span></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:0;font-size:9px;color:#94a3b8;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Instagram</td><td style="vertical-align:middle;padding-bottom:0;font-family:Arial,sans-serif;line-height:16px;"><a href="https://www.instagram.com/oleksandrhalushka.bau/" style="color:#d97706;text-decoration:none;font-size:12px;">@oleksandrhalushka.bau</a></td></tr></table></td><td style="vertical-align:bottom;text-align:right;padding-left:10px;padding-bottom:2px;width:75px;"><img src="https://files.catbox.moe/05gl5o.png" height="42" alt="Handwritten Signature" style="display:inline-block;border:0;height:42px;width:auto;" /></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:12px;margin-bottom:8px;"><tr><td style="border-top:1px solid #cbd5e1;height:1px;"></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td><a href="https://www.oleksandrhalushka.de" style="color:#64748b;text-decoration:none;font-size:11px;">www.oleksandrhalushka.de</a></td><td style="text-align:right;"><a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color:#94a3b8;text-decoration:none;font-size:11px;">Impressum</a></td></tr></table></td></tr></table></td></tr></table>`;
  const univ = `<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;max-width:440px;width:100%;border:0;"><tr><td style="padding:10px 0;"><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:top;"><div style="font-size:20px;font-weight:800;color:#0f172a;letter-spacing:-0.4px;line-height:1.2;">Oleksandr Halushka</div><div style="font-size:10px;color:#64748b;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-top:4px;">Fahrzeugberatung &amp; Innenausbau · Bayern</div><div style="font-size:9px;color:#94a3b8;margin-top:2px;">Einzelunternehmer</div></td><td style="vertical-align:top;text-align:right;width:34px;padding-left:10px;"><img src="https://files.catbox.moe/5mkatp.png" width="34" alt="OH Monogram Logo" style="display:inline-block;border:0;width:34px;height:auto;" /></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:12px;margin-bottom:12px;"><tr><td style="border-top:1px solid #cbd5e1;height:1px;"></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:top;width:290px;"><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Telefon</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="tel:+4916093409671" style="color:#0f172a;text-decoration:none;font-size:12px;font-weight:500;">+49 160 9340 9671</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">WhatsApp</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="https://wa.me/4916093409671" style="color:#64748b;text-decoration:none;font-size:12px;font-weight:500;">Nachricht senden →</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">E-Mail</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="mailto:info@oleksandrhalushka.de" style="color:#0f172a;text-decoration:none;font-size:12px;font-weight:500;">info@oleksandrhalushka.de</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#64748b;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Adresse</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><span style="color:#334155;font-size:12px;">Industriestraße 22, 93077 Bad Abbach</span></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:6px;font-size:9px;color:#94a3b8;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Instagram</td><td style="vertical-align:middle;padding-bottom:6px;font-family:Arial,sans-serif;line-height:16px;"><a href="https://www.instagram.com/oleksandrhalushka.auto/" style="color:#3b7dd8;text-decoration:none;font-size:12px;">@oleksandrhalushka.auto</a></td></tr><tr><td style="vertical-align:middle;width:78px;padding-bottom:0;font-size:9px;color:#94a3b8;letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">Instagram</td><td style="vertical-align:middle;padding-bottom:0;font-family:Arial,sans-serif;line-height:16px;"><a href="https://www.instagram.com/oleksandrhalushka.bau/" style="color:#d97706;text-decoration:none;font-size:12px;">@oleksandrhalushka.bau</a></td></tr></table></td><td style="vertical-align:bottom;text-align:right;padding-left:10px;padding-bottom:2px;width:75px;"><img src="https://files.catbox.moe/05gl5o.png" height="42" alt="Handwritten Signature" style="display:inline-block;border:0;height:42px;width:auto;" /></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:12px;margin-bottom:8px;"><tr><td style="border-top:1px solid #cbd5e1;height:1px;"></td></tr></table><table cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr><td><a href="https://www.oleksandrhalushka.de" style="color:#64748b;text-decoration:none;font-size:11px;">www.oleksandrhalushka.de</a></td><td style="text-align:right;"><a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color:#94a3b8;text-decoration:none;font-size:11px;">Impressum</a></td></tr></table></td></tr></table></td></tr></table>`;
  
  if (type === 'Auto') return auto;
  if (type === 'Bau') return bau;
  return univ;
}

function sendInitialConfirmation(data) {
  const sigHtml = getSignatureHtml(data.source);
  
  const cmDict = {
    de: { email: 'per E-Mail', wa_text: 'per WhatsApp (Nachricht)', wa_audio: 'per WhatsApp (Anruf)', phone: 'telefonisch' },
    en: { email: 'by email', wa_text: 'via WhatsApp (Text)', wa_audio: 'via WhatsApp (Call)', phone: 'by phone' },
    ru: { email: 'через E-Mail', wa_text: 'через WhatsApp (сообщение)', wa_audio: 'через WhatsApp (звонок)', phone: 'по телефону' },
    uk: { email: 'через E-Mail', wa_text: 'через WhatsApp (повідомлення)', wa_audio: 'через WhatsApp (дзвінок)', phone: 'телефоном' }
  };
  const contactStr = (cmDict[data.language] && cmDict[data.language][data.contactPref]) || cmDict.de[data.contactPref] || data.contactPref;
  
  const tDe = data.prefTime !== 'any' && data.prefTime ? ` zwischen ${data.prefTime} Uhr` : '';
  const tEn = data.prefTime !== 'any' && data.prefTime ? ` between ${data.prefTime}` : '';
  const tRu = data.prefTime !== 'any' && data.prefTime ? ` в период с ${data.prefTime}` : '';
  const tUk = data.prefTime !== 'any' && data.prefTime ? ` у період з ${data.prefTime}` : '';

  const translatedTopic = getTranslatedTopic(data.topic, data.language);

  const templates = {
    de: { subject: 'Ihre Anfrage bei Oleksandr Halushka', htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Hallo ${data.firstName},<br><br>vielen Dank für Ihre Anfrage. Wir melden uns bei Ihnen am <b>${data.prefDate}${tDe}</b> ${contactStr}, um die Details zu "${translatedTopic}" zu besprechen.<br><br>Bis bald,<br><br>${sigHtml}</div>` },
    uk: { subject: 'Ваша заявка в Oleksandr Halushka', htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Вітаємо, ${data.firstName}!<br><br>Дякуємо за звернення. Ми зв'яжемося з вами <b>${data.prefDate}${tUk}</b> ${contactStr}, щоб обговорити деталі щодо "${translatedTopic}".<br><br>До зв'язку,<br><br>${sigHtml}</div>` },
    ru: { subject: 'Ваша заявка в Oleksandr Halushka', htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Здравствуйте, ${data.firstName}!<br><br>Спасибо за обращение. Мы свяжемся с вами <b>${data.prefDate}${tRu}</b> ${contactStr}, чтобы обсудить детали по "${translatedTopic}".<br><br>До связи,<br><br>${sigHtml}</div>` },
    en: { subject: 'Your request at Oleksandr Halushka', htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Hello ${data.firstName},<br><br>Thank you for reaching out. We will contact you on <b>${data.prefDate}${tEn}</b> ${contactStr} to discuss the details regarding "${translatedTopic}".<br><br>Talk to you soon,<br><br>${sigHtml}</div>` }
  };
  const t = templates[data.language] || templates.de;
  if (data.email) GmailApp.sendEmail(data.email, t.subject, "", { name: 'Oleksandr Halushka', htmlBody: t.htmlBody });
}

function sendFinalConfirmationEmail(sheet, row, sourceName, finalDateTime) {
  const dataValues = sheet.getRange(row, 1, 1, 19).getValues()[0];
  const data = {
    firstName: dataValues[2],
    email: dataValues[4],
    language: dataValues[7],
    topic: dataValues[8]
  };
  
  const translatedTopic = getTranslatedTopic(data.topic, data.language);
  
  const start = new Date(finalDateTime);
  const end = new Date(start.getTime() + 60 * 60 * 1000);
  const formatted = start.toLocaleString();
  
  const fDate = (d) => d.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
  const calTitle = encodeURIComponent('Oleksandr Halushka Termin: ' + translatedTopic);
  const calLoc = encodeURIComponent('Industriestraße 22, 93077 Bad Abbach');
  const calDetails = encodeURIComponent('Ihr Termin bei Oleksandr Halushka. Wir freuen uns auf Sie!');
  const gCalLink = 'https://www.google.com/calendar/render?action=TEMPLATE&text=' + calTitle + 
                  '&dates=' + fDate(start) + '/' + fDate(end) + 
                  '&details=' + calDetails + '&location=' + calLoc;

  const btnStyle = 'display:inline-block;padding:12px 24px;background-color:#0f172a;color:#ffffff;text-decoration:none;border-radius:6px;font-weight:bold;margin:15px 0;font-family:sans-serif;';
  
  let sigType = 'Universal';
  if (sourceName === SHEET_ZAYAVKI_AUTO) sigType = 'Auto';
  else if (sourceName === SHEET_ZAYAVKI_BAU) sigType = 'Bau';
  const sigHtml = getSignatureHtml(sigType);

  const templates = {
    de: { 
      subject: 'Ihr Termin ist bestätigt – Oleksandr Halushka', 
      htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Hallo ${data.firstName},<br><br>Ihr Termin für <b>"${translatedTopic}"</b> steht fest:<br><br><b>Zeit:</b> ${formatted}<br><b>Ort:</b> Industriestraße 22, 93077 Bad Abbach<br><br><a href="${gCalLink}" style="${btnStyle}">Zum Google Kalender hinzufügen</a><br><br>Wir freuen uns auf Sie!<br><br>${sigHtml}</div>`
    },
    ru: { 
      subject: 'Ваша запись подтверждена – Oleksandr Halushka', 
      htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Здравствуйте, ${data.firstName}!<br><br>Ваша запись на <b>"${translatedTopic}"</b> успешно подтверждена:<br><br><b>Время:</b> ${formatted}<br><b>Адрес:</b> Industriestraße 22, 93077 Bad Abbach<br><br><a href="${gCalLink}" style="${btnStyle}">Добавить в Google Календарь</a><br><br>До встречи!<br><br>${sigHtml}</div>`
    },
    uk: { 
      subject: 'Ваш запис підтверджено – Oleksandr Halushka', 
      htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Вітаємо, ${data.firstName}!<br><br>Ваш запис на <b>"${translatedTopic}"</b> успішно підтверджено:<br><br><b>Час:</b> ${formatted}<br><b>Адрес:</b> Industriestraße 22, 93077 Bad Abbach<br><br><a href="${gCalLink}" style="${btnStyle}">Додати в Google Календар</a><br><br>До зустрічі!<br><br>${sigHtml}</div>`
    },
    en: { 
      subject: 'Your appointment is confirmed – Oleksandr Halushka', 
      htmlBody: `<div style="font-family:sans-serif;color:#333;line-height:1.6;font-size:15px;">Hello ${data.firstName},<br><br>Your appointment is confirmed:<br><br><b>Time:</b> ${formatted}<br><b>Location:</b> Industriestraße 22, 93077 Bad Abbach<br><br><a href="${gCalLink}" style="${btnStyle}">Add to Google Calendar</a><br><br>Looking forward to seeing you!<br><br>${sigHtml}</div>`
    }
  };
  const t = templates[data.language] || templates.de;
  if (data.email) {
    try { GmailApp.sendEmail(data.email, t.subject, '', { name: 'Oleksandr Halushka', htmlBody: t.htmlBody }); } catch(e){}
  }
}

function sendOwnerNotification(data, row, leadId) {
  const subject = '[NEUE ANFRAGE] ' + (data.source || '') + ': ' + (data.firstName || '') + ' ' + (data.lastName || '');

  const bodyText = `Neue Anfrage ${leadId}\n\nKunde: ${data.firstName} ${data.lastName}\nE-Mail: ${data.email}\nTelefon: ${data.phone}\nThema: ${data.topic}\nWunschtermin: ${data.prefDate} (${data.prefTime})\nSprache: ${data.language}`;

  const cleanPhone = (data.phone || "").replace(/[^0-9]/g, '');
  const waText = encodeURIComponent('Hallo ' + (data.firstName || '') + ', hier ist Oleksandr Halushka. Danke für Ihre Anfrage zu ' + (data.topic || '') + '!');
  const waLink = cleanPhone ? `https://wa.me/${cleanPhone}?text=${waText}` : '#';
  const spreadsheetLink = 'https://docs.google.com/spreadsheets/d/' + getSpreadsheetId() + '/edit';

  const appUrl = 'https://script.google.com/macros/s/AKfycby80l8o7Th7ZtUE2rBZ7bLdvv8-wMSxJAbhX8AHjBe3izeDll7KavfIAMhVCdL9E0cW4Q/exec';
  const mobileConfirmLink = appUrl + '?action=mobile_confirm&leadId=' + encodeURIComponent(leadId) + '&source=' + encodeURIComponent(data.source || 'Auto');

  const e = {
    leadId: escapeHtml(leadId),
    source: escapeHtml(data.source),
    firstName: escapeHtml(data.firstName),
    lastName: escapeHtml(data.lastName),
    email: escapeHtml(data.email),
    phone: escapeHtml(data.phone),
    contactPref: escapeHtml(data.contactPref),
    language: escapeHtml(String(data.language || '').toUpperCase()),
    topic: escapeHtml(data.topic),
    prefDate: escapeHtml(data.prefDate),
    prefTime: escapeHtml(data.prefTime),
    message: escapeHtml(data.message) || '- Keine Nachricht hinterlassen -',
    waLink: escapeHtml(waLink),
    spreadsheetLink: escapeHtml(spreadsheetLink),
    mobileConfirmLink: escapeHtml(mobileConfirmLink)
  };

  const btnStyle = 'display:inline-block;padding:14px 28px;background-color:#16a34a;color:#ffffff;text-decoration:none;border-radius:8px;font-weight:bold;margin:10px 10px 10px 0;font-family:sans-serif;font-size:16px;box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);';
  const waBtnStyle = 'display:inline-block;padding:14px 28px;background-color:#25D366;color:#ffffff;text-decoration:none;border-radius:8px;font-weight:bold;margin:10px 0;font-family:sans-serif;font-size:16px;box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);';

  const htmlBody = `
    <div style="font-family:sans-serif;color:#1e293b;max-width:600px;margin:20px auto;border:1px solid #e2e8f0;border-radius:12px;padding:32px;background:#ffffff;box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);">
      <h2 style="margin-top:0;color:#0f172a;border-bottom:2px solid #f1f5f9;padding-bottom:16px;font-size:22px;">Neue Buchungsanfrage ${e.leadId}</h2>
      <p style="font-size:15px;color:#475569;line-height:1.5;">Sie haben eine neue Anfrage über die Website (<b>${e.source}</b>) erhalten.</p>

      <table style="width:100%;border-collapse:collapse;margin-top:20px;font-size:15px;">
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;width:140px;color:#64748b;">Kunde:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-weight:bold;font-size:16px;">${e.firstName} ${e.lastName}</td></tr>
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;color:#64748b;">E-Mail:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><a href="mailto:${e.email}" style="color:#2563eb;text-decoration:none;">${e.email}</a></td></tr>
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;color:#64748b;">Telefon:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><a href="tel:${e.phone}" style="color:#2563eb;text-decoration:none;">${e.phone}</a></td></tr>
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;color:#64748b;">Kontaktweg:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;">${e.contactPref}</td></tr>
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;color:#64748b;">Sprache:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><b>${e.language}</b></td></tr>
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;color:#64748b;">Thema:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-weight:bold;color:#0f172a;">${e.topic}</td></tr>
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;color:#64748b;">Wunschtermin:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-weight:bold;color:#b91c1c;">${e.prefDate} (Fenster: ${e.prefTime})</td></tr>
        <tr><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;color:#64748b;vertical-align:top;">Nachricht:</td><td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-style:italic;color:#475569;">${e.message}</td></tr>
      </table>

      <div style="text-align:center;margin-top:20px;">
        <a href="${e.waLink}" style="${waBtnStyle}">WhatsApp Chat öffnen</a><br>
        <a href="${e.mobileConfirmLink}" style="${btnStyle}; background-color:#3b82f6;">&#x1F4F1; Подтвердить термин (Mobile Web App)</a><br>
        <a href="${e.spreadsheetLink}" style="${btnStyle}">Всю таблицу открыть</a>
      </div>
    </div>
  `;

  GmailApp.sendEmail(OWNER_EMAIL, subject, bodyText, { 
    name: 'Oleksandr Halushka CRM',
    htmlBody: htmlBody
  });
}
