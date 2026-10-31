+++
id = "sk-rem-curve-wild-example"
kind = "remark"
title = "The affine line in characteristic $p$"
order = 923
tags = ["sketch", "latex:example"]
+++
For $U=\mathbf A^1_k$ in characteristic $p$ we get

$$
H^1(U,\mathbf F_p)=k[t]/\{h^p-h:h\in k[t]\}.
$$

Every class has a unique representative with zero constant term
and all positive exponents prime to $p$. Indeed, we can remove
exponents divisible by $p$ using $p$th roots in the perfect field, and
we can remove the constant term since $a\mapsto a^p-a$ is surjective on $k$.
For uniqueness, note that a nonconstant polynomial $h^p-h$ has
degree divisible by $p$. In particular the quotient is infinite, because the
classes of $t^m$ for positive $m$ prime to $p$ are $\mathbf F_p$-linearly
independent. For an algebraically closed extension $k\subsetneq k'$
and $a\in k'\setminus k$, the class of $at$ is not in the image of the
quotient over $k$: the reduction of a polynomial in $k[t]$ uses only
$p$th roots and roots of $x^p-x=c$ in $k$, so its reduced representative
lies in $k[t]$, whereas $at$ is already reduced. Thus finiteness and invariance under field extension in
degree one fail for $p$-torsion coefficients on an affine curve, and this
is why $(C_5)$ and $(C_7)$ require properness.
