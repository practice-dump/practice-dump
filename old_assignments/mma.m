function y = f (x)
  y = sin (x^3);
endfunction
[q, ier, nfun, err] = quad ("f", 0, 1)

function z=f2(x)
  z=x^5.*(1-x^2)^1.5
endfunction
[q1, ier, nfun, err] = quad ("f2", 0, 1)
