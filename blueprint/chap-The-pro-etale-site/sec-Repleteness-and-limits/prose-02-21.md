+++
id = "prose-02-21"
kind = "hidden"
title = "Repleteness and limits (1)"
order = 83
+++
We need inverse limits to pass from torsion to adic coefficients, for
example to form $\varprojlim_n\mathbf Z/\ell^n$. The first use of weakly
contractible objects is to show that such limits are well behaved. In a
general topos a limit of epimorphisms need not be an epimorphism, because
the local lifts at each stage may require ever finer covers. On
$X_{\mathrm{pro}\acute{e}t}$ this does not happen. Surjectivity and exactness can be
checked on sections over weakly contractible objects, and there no
refinement is needed. As a result, the limit of a tower of epimorphisms maps
epimorphically onto each term
(Proposition [proposition-repleteness-pro-etale-topos]). For the same
reason products are exact (Proposition [proposition-exact-products]).

Exactness of products means that derived limits can be computed as for
abelian groups. The derived limit of a tower is the fibre of $1-T$ on the
product. Its cohomology is therefore given by the Milnor sequence of
Proposition [proposition-milnor-sequence], and $R^p\varprojlim$
vanishes for $p\geq2$. For a tower of epimorphisms, such as
$(\mathbf Z/\ell^n)_X$, the derived limit is the ordinary limit. In the next
subsection we deduce left completeness from the Milnor sequence. With these
facts we compute the cohomology of $\mathbf Z_\ell$ as continuous cohomology
(Proposition [proposition-continuous-cohomology-pro-etale-cohomology]).
