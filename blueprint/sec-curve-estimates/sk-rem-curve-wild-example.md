+++
id = "sk-rem-curve-wild-example"
kind = "remark"
title = "The affine line in characteristic $p$"
order = 1421
tags = ["sketch"]
+++
For $U=\A^1_k$ in characteristic $p$ one obtains

$$
H^1(U,\mathbf F_p)=k[t]/\{h^p-h:h\in k[t]\}.
$$

Every class has a unique representative with zero constant term and all
positive exponents prime to $p$. Exponents divisible by $p$ are removed using
$p$th roots in the perfect field; the constant term is removed by
surjectivity of $a\mapsto a^p-a$ on $k$. For uniqueness, a nonconstant
polynomial $h^p-h$ has leading degree divisible by $p$. Hence the quotient is
infinite: the classes of $t^m$ for positive $m$ prime to $p$ are
$\mathbf F_p$-linearly independent. For an algebraically closed extension
$k\subsetneq k'$ and $a\in k'\setminus k$, the class of $at$ is not in the
image of the quotient over $k$. Thus finiteness and field-extension
invariance in degree one fail for characteristic torsion on an affine curve,
which is why $(C_5)$ and $(C_7)$ require properness. The same failure is why the field-extension invariance
[sk-cor-curve-invariance], used in the proof of proper base change, needs
properness: there the coefficients are arbitrary torsion sheaves.
