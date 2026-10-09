def _():
  import re
  import types
  from os import listdir

  # prints an error and exits the program
  def error(*msg):
    from sys import stderr
    msg = '\n'.join(msg)
    print(f'ERROR: {msg}', file=stderr)
    exit()

  silent = True
  while True:
    if not silent:
      print(
       'Which file(s) would you like to run?',
       '(Please enter the leading # on the file name or hit enter with blank input to run them all)',
       sep='\n',
      )

    silent = False

    to_run = input('🟢 ').strip(' ')
    if to_run not in ('', '*', 'all'):
      try:
        to_run = int(to_run)
      except ValueError:
        from sys import stderr
        print('Bad input.', file=stderr)
        continue
    break

  run_all = not isinstance(to_run, int)

  modules = []
  files = listdir("./scripts")

  # filter out anything that isn't a python file (__pycache__, *.pyc, etc.)
  files = [f for f in files if f.endswith('.py')]

  if not files:
    error('No python files found in "scripts" folder.')

  if not run_all:
    for file in files:
      if not file.startswith(f'{to_run}'):
        continue
      files = [file]
      break
    else:
      error('No such file found.')

  # test file names against this re pattern
  regex = re.compile('\d_[a-zA-Z]+\.py')
  for file in files:
    if not regex.match(file):
      error(
       f'file "{file}" doesn\'t follow the naming convention of "<num>_<firstname>.py"'
      )

    with open(f'scripts/{file}', 'r') as stream:
      src = stream.read()

      if run_all:
        try:
          end = src.replace('# stop', '#stop', 1).index('#stop')
        except ValueError:
          pass
        else:
          src = src[:end]

      code = compile(src, file, 'exec')
      module = types.ModuleType(f'scripts.{file[:-3]}')
      module.__file__ = f'scripts/{file}'
      exec(code, module.__dict__)
      modules.append(module)

  # sort by the prefixed number on file name
  modules = sorted(modules, key=lambda m: int(m.__name__[8]))

  # some error checking
  for module in modules:
    module_name = f'{module.__name__[8:]}.py'

    # hasattr() checks if an attribute exists on the object
    if not hasattr(module, "main"):
      error(f'"main()" function is not defined in "{module_name}"')

    fn = module.main
    # check if "fn" is actually a function
    if not isinstance(fn, types.FunctionType):
      # how does this even happen
      error(
       f'"main()" in "{module_name}" is not a function (received {fn} instead)',
       '',
       'Challenge Complete!',
       'How Did We Get Here?',
      )

  if not run_all:
    # update globals() with modules[0].__dict__ to allow use in REPL
    globals().update(modules[0].__dict__)

  else:
    state = modules[0].main()

    for module in modules[1:]:
      if not isinstance(state, tuple):
        state = state,

      params = module.main.__code__.co_argcount
      req_params = len(state)
      if req_params != params:
        module_name = f'{module.__name__[8:]}.py'
        error(
         f'main() function in "{module_name}" needs to have {req_params} parameter(s)',
         f'It currently has {params}.',
        )

      state = module.main(*state)


_()
del _