#!/usr/bin/env pyrate

assert(pyrate_version == pyrate_version)
ctx = Context(compiler = {'C++': find_external('gcc', std = 'c++03')})

compiler['C++'].std = 'latest'
print(compiler['C++'].std) # latest
compiler['C++'].std = 'c++11'
print(compiler['C++'].std)
print(ctx.compiler['C++'].std)

pthread = find_external('pthread')
exe1 = executable('example08_default_ctx.bin', ['test_cpp11.cpp', 'foo.cpp', pthread], compiler_opts = '-O3')
exe2 = ctx.executable('example08_own_ctx.bin', ['test_cpp11.cpp', 'foo.cpp', pthread], compiler_opts = '-O3')
default_targets = exe1
print(exe1)
