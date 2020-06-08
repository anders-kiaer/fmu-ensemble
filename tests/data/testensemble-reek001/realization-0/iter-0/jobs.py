jobList = [ {"name" : "DESIGN2PARAMS",
  "executable" : "/project/res/etc/ERT/Scripts/design2params.py",
  "target_file" : "DESIGN2PARAMS.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "DESIGN2PARAMS.stdout",
  "stderr" : "DESIGN2PARAMS.stderr",
  "stdin" : None,
  "argList" : ["0","/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../input/distributions/design_matrix.xlsx","DesignMatrix","DefaultValues"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "DESIGN_KW",
  "executable" : "/project/res/etc/ERT/Scripts/design_kw.py",
  "target_file" : "DESIGN_KW.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "DESIGN_KW.stdout",
  "stderr" : "DESIGN_KW.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../input/templates/global_variables.tmpl","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/global_variables.ipl"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "DESIGN_KW",
  "executable" : "/project/res/etc/ERT/Scripts/design_kw.py",
  "target_file" : "DESIGN_KW.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "DESIGN_KW.stdout",
  "stderr" : "DESIGN_KW.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../input/templates/multflt.tmpl","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/reek.multflt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "DESIGN_KW",
  "executable" : "/project/res/etc/ERT/Scripts/design_kw.py",
  "target_file" : "DESIGN_KW.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "DESIGN_KW.stdout",
  "stderr" : "DESIGN_KW.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../input/templates/let-swof.tmpl","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/let-swof.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "DESIGN_KW",
  "executable" : "/project/res/etc/ERT/Scripts/design_kw.py",
  "target_file" : "DESIGN_KW.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "DESIGN_KW.stdout",
  "stderr" : "DESIGN_KW.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../input/templates/let-sgof.tmpl","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/let-sgof.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "DESIGN_KW",
  "executable" : "/project/res/etc/ERT/Scripts/design_kw.py",
  "target_file" : "DESIGN_KW.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "DESIGN_KW.stdout",
  "stderr" : "DESIGN_KW.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../input/templates/multz.tmpl","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/reek.multz"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/model"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_directory.stdout",
  "stderr" : "copy_directory.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../rms/bin","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/rms"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_directory.stdout",
  "stderr" : "copy_directory.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../rms/ipl","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/rms"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/input/global_variables"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_directory.stdout",
  "stderr" : "copy_directory.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../rms/input/config","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/rms/input"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_directory.stdout",
  "stderr" : "copy_directory.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../rms/input/well_modelling","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/rms/input"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/output/aps"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/output/cohiba/surfaces"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/output/cohiba/logfiles"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/output/pem"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/output/regions/data/grid"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/output/regions/result"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["rms/output/zone"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["sim2seis/model"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_file.stdout",
  "stderr" : "copy_file.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../sim2seis/model/model_2000_sim.txt","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/sim2seis/model/model_2000_sim.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_file.stdout",
  "stderr" : "copy_file.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../sim2seis/model/model_2001_sim.txt","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/sim2seis/model/model_2001_sim.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_file.stdout",
  "stderr" : "copy_file.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../sim2seis/model/model_2003_sim.txt","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/sim2seis/model/model_2003_sim.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["sim2seis/input"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["sim2seis/output"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["eclipse/include/grid"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["eclipse/include/props"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_file.stdout",
  "stderr" : "copy_file.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../eclipse/include/props/reek.endpoints","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include/props/reek.endpoints"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_file.stdout",
  "stderr" : "copy_file.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../eclipse/include/props/reek.pvt","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include/props/reek.pvt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["eclipse/include/regions"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["eclipse/include/solution"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "COPY_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/copy_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "copy_directory.stdout",
  "stderr" : "copy_directory.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../eclipse/include/summary","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["eclipse/include/schedule"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["share/results/maps"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["share/results/grids"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["share/results/polygons"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["share/results/volumes"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["share/results/images"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MAKE_DIRECTORY",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/make_directory.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "make_directory.stdout",
  "stderr" : "make_directory.stderr",
  "stdin" : None,
  "argList" : ["share/results/observations"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MOVE_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/move_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "move_file.stdout",
  "stderr" : "move_file.stderr",
  "stdin" : None,
  "argList" : ["global_variables.ipl","rms/input/global_variables/global_variables.ipl"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MOVE_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/move_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "move_file.stdout",
  "stderr" : "move_file.stderr",
  "stdin" : None,
  "argList" : ["reek.multflt","eclipse/include/grid/reek.multflt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MOVE_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/move_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "move_file.stdout",
  "stderr" : "move_file.stderr",
  "stdin" : None,
  "argList" : ["let-swof.txt","eclipse/include/props/let-swof.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MOVE_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/move_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "move_file.stdout",
  "stderr" : "move_file.stderr",
  "stdin" : None,
  "argList" : ["let-sgof.txt","eclipse/include/props/let-sgof.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "MOVE_FILE",
  "executable" : "/project/res/etc/ERT/Config/jobs/util/script/move_file.py",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "move_file.stdout",
  "stderr" : "move_file.stderr",
  "stdin" : None,
  "argList" : ["reek.multz","eclipse/include/grid/reek.multz"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "DESIGN_KW",
  "executable" : "/project/res/etc/ERT/Scripts/design_kw.py",
  "target_file" : "DESIGN_KW.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "DESIGN_KW.stdout",
  "stderr" : "DESIGN_KW.stderr",
  "stdin" : None,
  "argList" : ["/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../input/templates/seed.tmpl","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/rms/model/RMS_SEED"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "RMS_BATCH",
  "executable" : "/project/res/etc/ERT/Scripts/run_rms_batch.py",
  "target_file" : "RMS_TARGET.INC",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "rms.stdout",
  "stderr" : "rms.stderr",
  "stdin" : None,
  "argList" : ["rms/model","0","10.1.1","/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/model/../../rms/model/reek.rms10.1.1","./","./","MAIN"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "GENERATE_RELPERM",
  "executable" : "/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/bin/scripts/generate_relperm.sh",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "GENERATE_RELPERM.stdout",
  "stderr" : "GENERATE_RELPERM.stderr",
  "stdin" : None,
  "argList" : ["/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include/props/let-swof.txt","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include/props/swof.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "GENERATE_RELPERM",
  "executable" : "/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/bin/scripts/generate_relperm.sh",
  "target_file" : None,
  "error_file" : None,
  "start_file" : None,
  "stdout" : "GENERATE_RELPERM.stdout",
  "stderr" : "GENERATE_RELPERM.stderr",
  "stdin" : None,
  "argList" : ["/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include/props/let-sgof.txt","/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include/props/sgof.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "INCLUDE_PC",
  "executable" : "/project/fmu/users/havb/reek_20180207/resmod/ff/2017a/r001/ert/bin/scripts/include_pc.py",
  "target_file" : "INCLUDE_PC.INC",
  "error_file" : None,
  "start_file" : None,
  "stdout" : "INCLUDE_PC.stdout",
  "stderr" : "INCLUDE_PC.stderr",
  "stdin" : None,
  "argList" : ["/scratch/fmu/havb/2_r001_reek/realization-0/iter-0/eclipse/include/props/swof.txt"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
},
 {"name" : "ECLIPSE100_2014.2",
  "executable" : "/project/res/etc/ERT/Config/jobs/ressim/Scripts/run_ecl100",
  "target_file" : "eclipse/model/2_R001_REEK-0.OK",
  "error_file" : None,
  "start_file" : None,
  "stdout" : None,
  "stderr" : "ECLIPSE.stderr",
  "stdin" : None,
  "argList" : ["2014.2","eclipse/model/2_R001_REEK-0","1"],
  "environment" : None,
  "license_path" : None,
  "max_running_minutes" : None,
  "max_running" : None,
}]
umask = 0000