+++
kind  = "proof"
of    = "lem-mg-normal-restriction-semisimple"
+++
By the direct-sum definition of semisimplicity in
[def-wf-semisimple-module], it is enough to treat a simple
$\Gamma$-module $V$. Choose a nonzero $N$-stable subspace
$S\subseteq V$ of least positive dimension. It is simple as an
$N$-module by [def-wf-simple-module]. Normality makes every
translate $\gamma S$ another simple $N$-submodule. The sum of all
these translates is a nonzero $\Gamma$-submodule, hence is $V$, and
finitely many translates already span because $V$ is finite-dimensional.

Add those translates one at a time. If $D$ is the direct sum already
obtained and $S'$ is the next translate, then $S'\cap D$ is an
$N$-submodule of the simple module $S'$; it is either zero, in which
case $D+S'=D\oplus S'$, or all of $S'$, in which case nothing is
added. Thus $V|_N$ is a direct sum of simple $N$-modules. For a
represented degree datum take $N=P=\ker(\deg)$, which is normal in $W$
([d-monodromy]); the final assertion is precisely geometric semisimplicity in
[def-wf-geometric-semisimplicity].
