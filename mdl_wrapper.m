function results = mdl_wrapper(params_json)
    params = jsondecode(params_json);
    
    mdl = params.model_name;
    load_system(mdl);
    
    fnames = fieldnames(params);
    for i = 1:length(fnames)
        if ~strcmp(fnames{i}, 'model_name')
            paramName = fnames{i};
            paramValue = params.(fnames{i});
            assignin('base', paramName, paramValue);
        end
    end
    
    simOut = sim(mdl, 'ReturnWorkspaceOutputs', 'on');
    
    results = simOut.get('simout');
    
    if isa(results, 'timeseries')
        results = results.Data;
    end
    
    close_system(mdl, 0);
end
