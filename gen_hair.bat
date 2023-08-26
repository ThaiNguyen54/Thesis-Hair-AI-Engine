@echo OFF
rem How to run a Python script in a given conda environment from a batch file.

rem It doesn't require:
rem - conda to be in the PATH
rem - cmd.exe to be initialized with conda init

rem Define here the path to your conda installation
set CONDAPATH=C:\ProgramData\anaconda3
rem Define here the name of the environment
set ENVNAME=thesis-env

rem The following command activates the base environment.
rem call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\ProgramData\Miniconda3
if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=C:\Users\Thai\.conda\envs\%ENVNAME%)

rem Activate the conda environment
rem Using call is required here, see: https://stackoverflow.com/questions/24678144/conda-environments-and-bat-files
call %CONDAPATH%\Scripts\activate.bat %ENVPATH%

rem Run a python script in that environment
python D:\Study\Thesis\Hair-AI-Engine\StyleYourHair\main.py --input_dir .\ffhq_image\ --im_path1 %1 --im_path2 %2 --output_dir .\style_your_hair_output --warp_loss_with_prev_list delta_w style_hair_slic_large --save_all --version final --W_steps 450 --FS_steps 50 --align_steps1 50 --align_steps2 25 --warp_steps 100

rem Deactivate the environment
call conda deactivate

rem If conda is directly available from the command line then the following code works.
rem call activate someenv
rem python script.py
rem conda deactivate

rem One could also use the conda run command
rem conda run -n someenv python script.py
