import notabene as nb

x, y, z, i, n = nb.to('x y z i n')
f, g, h       = nb.fun('f g h')

with nb.files.defs('diff.tex') as defs:
    nb.config.push('display style', True) 
    defs.prefix = 'ex'

    # differentials
    
    defs['D'] = nb.seq(nb.diff.d(x),
                       nb.diff.d(x,y,z),
                       nb.diff.D(x),
                       nb.diff.D(x,y,z))
    
    defs['DFrac'] = nb.seq(nb.diff.dfrac(x,y,z),
                           nb.diff.Dfrac(x,y,z))

    # derivatives and gradients

    f1 = nb.diff.dfun(x, y, z)
    f2 = nb.diff.Dfun(x, y, z)
    defs['DFun'] = nb.seq(f1(i**n), f2(i**n))

    grad_x = nb.diff.Gfun(x)
    defs['Grad'] = nb.seq(nb.diff.G(x),
                          grad_x(i**n))

    # integrals.

    defs['IntA'] = nb.diff.integral(x==1, f(x), x)
    defs['IntB'] = nb.diff.integral((x==1, n), f(x), x)
    defs['IntC'] = nb.diff.integral([(x==1, n), y < x, (z==0, x**2)],
                                    f(x, y, z),
                                    [x,y,z])

    
    

    defs.cheatsheet() 
