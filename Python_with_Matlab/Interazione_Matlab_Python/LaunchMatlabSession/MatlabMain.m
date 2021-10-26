% Python info
pyenv;
pathToPythonFunction = fileparts(which("Python_functions.py"));

if isempty(pathToPythonFunction)
    disp("Python utility not found. Ending process...")
    return
end

disp("a = 10; b = 10.5;")
% Using the function Somma from python
SommaInMatlab = py.Python_functions.SommaInPython(10,10.5);
disp(['Somma effettuata dalla libreria python: ' num2str(SommaInMatlab) ])

% Using the function Sottrazione from python
SottrazioneInMatlab = py.Python_functions.SottrazioneInPython(10,10.5);
disp(['Sottrazione effettuata dalla libreria python: ' num2str(SottrazioneInMatlab) ])