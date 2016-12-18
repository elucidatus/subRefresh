    var queryStart = pageVars.startDate;
    var queryEnd = pageVars.endDate;
    var forceDb = $("#forceDb").length > 0;

    caldata.loadAvailableJobs(queryStart, queryEnd, pageView.refreshDataComplete, forceDb);