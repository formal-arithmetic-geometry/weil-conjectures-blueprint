+++
kind  = "proof"
of    = "sk-thm-sfb-proper-base-change"
uses = ["sk-thm-properbasechange", "sk-thm-sfb-rationalization-comparison", "sk-thm-sfb-qlbar-two-colimit"]
+++
Following Bhatt–Scholze, §6.7, reduce to the torsion case. Let $\Lambda=\underline E$, and write
$\cO_E$ for the ring of integers, with uniformizer $\varpi$. A bounded constructible
$E$-complex $K$ is $E\otimes^{\mathrm L}_{\cO_E}K_0$ for a bounded constructible
$\cO_E$-complex $K_0$ ([sk-thm-sfb-rationalization-comparison]). All four functors commute with $E\otimes^{\mathrm L}_{\cO_E}-$ on such
complexes, so it suffices to show that $\mathrm{BC}_{sq}$ is an isomorphism on $K_0$. Now
$K_0\cong R\lim_nK_0/\varpi^n$. The functors $Rf_*$ and $Rf'_*$ commute with $R\lim$, and $Lg^*$,
$Lg'^*$ commute with it on bounded constructible complexes. All of them commute with reduction
modulo $\varpi^n$. So it suffices to show that $\mathrm{BC}_{sq}$ is an isomorphism on each
reduction $K_0/\varpi^n$. This is a bounded constructible complex of étale sheaves of
$\cO_E/\varpi^n$-modules, so its cohomology sheaves are torsion. On it, the pro-étale functors
agree with the étale ones, and $\mathrm{BC}_{sq}$ becomes the étale exchange morphism. This is
an isomorphism by the proper base change theorem [sk-thm-properbasechange], since $f$ is proper.

For $\Lambda=\underline{\Qlb}$, a bounded constructible $\Qlb$-complex is defined over some finite
extension $E\subseteq\Qlb$ of $\mathbf Q_\ell$ ([sk-thm-sfb-qlbar-two-colimit]). The base change morphisms for $\underline E$ and for
$\underline{\Qlb}$ are compatible with extension of scalars $\underline{\Qlb}\otimes^{\mathrm L}_{\underline E}-$,
so the claim follows from the case of $\underline E$.
