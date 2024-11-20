path)
    self.source_paths.append(self.mannwhitneyu_path)
    self.source_paths.append(self.d3_path)
    self.source_paths.append(self.chai_path)
    self.source_paths.append(self.mocha_path)
    self.source_paths.append(self.oboe_path)

  def CreateVulcanizer(self):
    from py_vulcanize import project as project_module
    return project_module.Project(self.source_paths)

  def IsD8CompatibleFile(self, filename):
    if filename.startswith(self.ui_path):
      return False

    if filename.startswith(self.value_ui_path):
      return False

    if filename.startswith(self.metrics_ui_path):
      return False

    return True

  def FindAllTestModuleRelPaths(self, pred=None):
    if pred is None:
      pred = lambda x: True

    all_filenames = _FindAllFilesRecursive([self.tracing_src_path])
    test_module_filenames = [x for x in all_filenames if
                             _IsFilenameATest(x) and pred(x)]
    test_module_filenames.sort()

    return [os.path.relpath(x, self.tracing_root_path)
            for x in test_module_filenames]

  def FindAllMetricsModuleRelPaths(self):
    all_filenames = _FindAllFilesRecursive([self.tracing_src_path])
    all_metrics_module_filenames = []
    for x in all_filenames:
      if x.startswith(self.metrics_path) and not _IsFilenameATest(x):
        all_metrics_module_filenames.append(x)
    all_metrics_module_filenames.sort()
    return [os.path.relpath(x, self.tracing_root_path)
            for x in all_metrics_module_filenames]

  def FindAllDiagnosticsModuleRelPaths(self):
    all_filenames = _FindAllFilesRecursive([self.tracing_src_path])
    all_diagnostics_module_filenames = []
    for x in all_filenames:
      if x.startswith(self.diagnostics_path) and not _IsFilenameATest(x):
        all_diagnostics_module_filenames.append(x)
    all_diagnostics_module_filenames.sort()
    return [os.path.relpath(x, self.tracing_root_path)
            for x in all_diagnostics_modu