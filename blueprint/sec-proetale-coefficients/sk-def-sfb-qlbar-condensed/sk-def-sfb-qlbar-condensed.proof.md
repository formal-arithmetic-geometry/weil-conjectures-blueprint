+++
kind  = "proof"
of    = "sk-def-sfb-qlbar-condensed"
+++
**Subring.** If $a$ takes values in $E$ and $b$ in $F$, then $a\pm b$ and $ab$ take
values in the compositum $EF$, which is a finite subextension. Constants lie in
$\mathbf Q_\ell$. So $\underline{\Qlb}(S)$ is a subring of $C(S,\Qlb)$, commutative since
$\Qlb$ is. It is stable under precomposition, because $(a\circ u)(S')\subseteq a(S)$. So
$\underline{\Qlb}$ is a subpresheaf of rings of $C(-,\Qlb)$.

**Sheaf.** The presheaf $C(-,\Qlb)$ is a sheaf, being the condensed ring of the
topological ring $\Qlb$ ([sk-def-sfb-condensed-ring]). A subpresheaf $G$ of a sheaf $F$ is
a sheaf if, for every covering sieve $R$ on $S$, every section $a\in F(S)$ whose
restrictions along all arrows of $R$ lie in $G$ already lies in $G(S)$. A covering sieve
of $*_{\mathrm{proét}}$ contains a finite family $\{\pi_i\colon S_i\to S\}$ with
$\coprod_iS_i\to S$ surjective. If each $a\circ\pi_i$ takes values in a finite
subextension $E_i$, then $a$ takes values in the compositum of the finitely many $E_i$,
which is again a finite subextension. So $a\in\underline{\Qlb}(S)$. Hence
$\underline{\Qlb}$ is a sheaf of commutative rings. By part 3 of
[sk-def-sfb-ring-object], its underlying abelian sheaf is a commutative ring object.

**Why not $C(-,\Qlb)$.** The inclusion $\underline{\Qlb}\subseteq C(-,\Qlb)$ is strict.
Let $S=\{0\}\cup\{1/n:n\ge1\}$, a convergent sequence and hence a profinite set. Choose
$\varpi_n\in\Qlb$ with $\varpi_n^n=\ell$. The polynomial $x^n-\ell$ is Eisenstein, so
$[\mathbf Q_\ell(\varpi_n):\mathbf Q_\ell]=n$. Set $a(1/n)=\ell^n\varpi_n$ and $a(0)=0$.
Since $|\ell^n\varpi_n|=\ell^{-n-1/n}\to0$, $a$ is continuous. But its values have
unbounded degree over $\mathbf Q_\ell$, so they lie in no finite subextension. This is
why $\underline{\Qlb}$ is defined by the finiteness condition rather than as
$C(-,\Qlb)$.
