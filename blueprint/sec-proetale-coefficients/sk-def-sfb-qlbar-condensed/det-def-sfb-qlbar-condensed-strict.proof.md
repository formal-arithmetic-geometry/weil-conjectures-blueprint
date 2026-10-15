+++
kind = "proof"
of = "det-def-sfb-qlbar-condensed-strict"
+++
*$S$ is profinite.* It is compact (a convergent sequence together with its limit), Hausdorff, and
totally disconnected, since between any two of its points there is a real number not in $S$.

*Continuity.* Each point $1/n$ is isolated in $S$, so $a$ is continuous at $1/n$. At $0$: with the
absolute value normalized by $|\ell|=\ell^{-1}$, we have $|\varpi_n|^n=|\ell|$, so
$|\varpi_n|=\ell^{-1/n}$ and $|a(1/n)|=\ell^{-n-1/n}\to0$ as $n\to\infty$. Since $1/n\to0$ in $S$ and
$a(1/n)\to0=a(0)$, $a$ is continuous at $0$.

*Unbounded degree.* The polynomial $x^n-\ell$ is Eisenstein at $\ell$, hence irreducible over
$\mathbf Q_\ell$, so $[\mathbf Q_\ell(\varpi_n):\mathbf Q_\ell]=n$. Since $\ell^n\in\mathbf Q_\ell^\times$,
$\mathbf Q_\ell(a(1/n))=\mathbf Q_\ell(\varpi_n)$. If $a(S)\subseteq E$ for a finite subextension $E$,
then $\mathbf Q_\ell(\varpi_n)\subseteq E$ and $n\le[E:\mathbf Q_\ell]$ for every $n$, which is
absurd. So $a\notin\underline{\Qlb}(S)$.
