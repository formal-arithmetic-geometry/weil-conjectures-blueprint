+++
id = "prose-02-15"
kind = "hidden"
title = "Repleteness, products and sequential limits"
order = 59
+++
We need inverse limits to pass from torsion to adic coefficients, for
example to form $\varprojlim_n\mathbf Z/\ell^n$, and the first use of
weakly contractible objects is to show that such limits are well behaved.
In a general topos a limit of epimorphisms need not be an epimorphism,
because the local lifts at each stage may require ever finer covers. On
$X_{\mathrm{pro}\acute{e}t}$ this does not happen. Surjectivity and exactness can be
checked on sections over weakly contractible objects, and there no
refinement is needed. Hence the limit of a tower of epimorphisms maps
epimorphically onto each term, and products are exact.

Exactness of products has a concrete consequence. The derived limit of a
tower is the fibre of $1-T$ on the product, as for abelian groups, so
$R^p\varprojlim$ vanishes for $p\geq2$ and the cohomology of a derived
limit is given by the Milnor sequence of Proposition [sk-prop-pe-milnor].
For a tower of epimorphisms, such as $(\mathbf Z/\ell^n)_X$, the derived
limit is the ordinary limit. These two facts are what we use later: the
Milnor sequence gives left completeness in the next subsection, and
together they compute the cohomology of $\Zl$ as continuous cohomology
(Proposition [sk-prop-pe-continuous-cohomology]).
