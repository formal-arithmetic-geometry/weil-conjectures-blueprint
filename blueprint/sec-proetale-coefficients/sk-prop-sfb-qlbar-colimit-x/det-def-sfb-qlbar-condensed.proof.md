+++
kind  = "proof"
of = "det-def-sfb-qlbar-condensed"
uses = ["det-def-sfb-qlbar-condensed-subextensions", "det-def-sfb-qlbar-condensed-definition", "det-def-sfb-qlbar-condensed-sheaf"]
+++
The finite subextensions form a directed poset by
[det-def-sfb-qlbar-condensed-subextensions]. That $\underline{\Qlb}$ is a subpresheaf of
commutative rings of $C(-,\Qlb)$ is [det-def-sfb-qlbar-condensed-definition], and that it
is a sheaf, whose underlying abelian sheaf is a commutative ring object, is
[det-def-sfb-qlbar-condensed-sheaf].

**Why not $C(-,\Qlb)$.** The inclusion $\underline{\Qlb}\subseteq C(-,\Qlb)$ is strict.
Let $S=\{0\}\cup\{1/n:n\ge1\}$, a convergent sequence and hence a profinite set. Choose
$\varpi_n\in\Qlb$ with $\varpi_n^n=\ell$. The polynomial $x^n-\ell$ is Eisenstein, so
$[\mathbf Q_\ell(\varpi_n):\mathbf Q_\ell]=n$. Set $a(1/n)=\ell^n\varpi_n$ and $a(0)=0$.
Since $|\ell^n\varpi_n|=\ell^{-n-1/n}\to0$, $a$ is continuous. But its values have
unbounded degree over $\mathbf Q_\ell$, so they lie in no finite subextension. This is
why $\underline{\Qlb}$ is defined by the finiteness condition rather than as
$C(-,\Qlb)$.
