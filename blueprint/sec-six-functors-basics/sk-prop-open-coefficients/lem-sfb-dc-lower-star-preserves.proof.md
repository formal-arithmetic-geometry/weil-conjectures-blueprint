+++
kind  = "proof"
of    = "lem-sfb-dc-lower-star-preserves"
uses = ["sk-thm-sfb-rationalization-comparison", "sk-thm-sfb-qlbar-two-colimit"]
+++
This is Deligne's finiteness theorem for $Rf_*$ (SGA 4½, *Th. finitude*, 1.1) in the
pro-étale form of Bhatt–Scholze, §6.8. Let first $\Lambda=\underline{\cO}_E$ with uniformizer
$\varpi$. By Bhatt–Scholze, a complex $K$ is bounded constructible if and only if two conditions
hold: $K$ is derived $\varpi$-complete, and its reduction $K/\varpi:=K\otimes^{\mathrm L}_{\cO_E}\cO_E/\varpi$
is a bounded complex with constructible cohomology coming from the étale site. Now $Rf_*$
preserves derived $\varpi$-complete complexes, since it commutes with $R\lim$. It commutes with
reduction modulo $\varpi$, by the projection formula for the perfect complex $\cO_E/\varpi$. On
complexes coming from the étale site it agrees with the étale $Rf_*$. Since $\ell$ is invertible
on the finite type $k$-schemes $X$ and $Y$, Deligne's theorem shows that $Rf_*(K/\varpi)$ is
bounded with constructible cohomology. Hence $Rf_*K$ is bounded constructible.

For $\Lambda=\underline E$, a bounded constructible $E$-complex is
$E\otimes^{\mathrm L}_{\cO_E}K_0$ for a bounded constructible $\cO_E$-complex $K_0$
([sk-thm-sfb-rationalization-comparison]), and $Rf_*$
commutes with $E\otimes^{\mathrm L}_{\cO_E}-$ on such complexes, since $X$ is quasi-compact and
quasi-separated. For $\Lambda=\underline{\Qlb}$, a bounded constructible complex is defined over
some finite extension $E$ of $\mathbf Q_\ell$ ([sk-thm-sfb-qlbar-two-colimit]), and the claim follows from the case $\underline E$.
