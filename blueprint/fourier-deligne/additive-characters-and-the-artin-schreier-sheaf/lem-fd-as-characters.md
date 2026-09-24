+++
id = "lem-fd-as-characters"
kind = "lemma"
title = "Isotypic decomposition of the Artin–Schreier pushforward"
order = 4140
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-finite-torsors", "lem-fd-as-cover", "lem-fd-character-orthogonality"]
+++
With the $\mathbf F_p$-action of [lem-fd-as-cover], there is a canonical decomposition

$$
\pi_*\overline{\mathbf Q}_\ell\cong\bigoplus_{\chi\in\widehat{\mathbf F}_p}\mathcal L_\chi,
$$

where each $\mathcal L_\chi$ is lisse of rank one on $X_0$, and $\mathcal L_\chi=1$ if and only if $\chi=0$. In particular
$\mathcal L_{\psi,f}\otimes\mathcal L_{\psi,g}\cong\mathcal L_{\psi,f+g}$ and $(\mathcal L_{\psi,f})^{-1}\cong\mathcal L_{-\psi,f}$.

## Proof

*Step 1 (the cover trivializes itself).* By [lem-fd-as-cover],
$\pi$ is finite étale of degree $p$ with the $\mathbf F_p$-action
$y\mapsto y+a$, and $Y=\Spec\mathcal O_{X_0}[T]/(T^p-T-f)$. In
$\mathcal O_Y[T']$ one has the identity

$$
T'^p-T'-f=\prod_{a\in\mathbf F_p}\bigl(T'-(T+a)\bigr),
$$

because the right-hand side equals $(T'-T)^p-(T'-T) =T'^p-T'-(T^p-T)$ and $T^p-T=f$ in $\mathcal O_Y$; the factors are pairwise
comaximal, their differences being the units $a'-a\in\mathbf F_p^\times$.
The Chinese remainder theorem therefore gives

$$
\mathcal O_Y\otimes_{\mathcal O_{X_0}}\mathcal O_Y
=\mathcal O_Y[T']/(T'^p-T'-f)\xrightarrow{\ \sim\ }
\prod_{a\in\mathbf F_p}\mathcal O_Y,
\qquad T'\longmapsto(T+a)_a ,
$$

that is $Y\times_{X_0}Y\cong\mathbf F_p\times Y$ by $(y,y')\mapsto(y'-y,y)$.
Consequently the $\mathbf F_p$-action is simply transitive on the geometric
fibres of $\pi$, so $\pi$ is an $\mathbf F_p$-torsor and
$\underline{\operatorname{Hom}}_{X_0}(-,Y)$ is a finite locally constant sheaf
with simply transitive $\mathbf F_p$-action in the sense of
[def-weil-pbc-finite-torsors].
*Step 2 (the pushforward is lisse of rank $p$).* Pulling back along the
étale cover $\pi$ and using Step 1 identifies
$\pi^*\pi_*\overline{\mathbf Q}_\ell$ with the constant sheaf
$\overline{\mathbf Q}_\ell[\mathbf F_p]$ carrying the regular representation;
by [def-weil-pbc-etale-sheaves] a sheaf which becomes constant after an
étale base change is locally constant, so $\pi_*\overline{\mathbf Q}_\ell$
is lisse of rank $p$, its stalk at every geometric point being the regular
representation.
*Step 3 (the idempotents split it).* Since $p\neq\ell$, the elements
$e_\chi=\frac1p\sum_{a\in\mathbf F_p}\chi(-a)\sigma_a$ of the group algebra are
well defined; expanding the product and substituting $c=a+b$, the coefficient
of $\sigma_c$ in $e_\chi e_{\chi'}$ is
$\frac1{p^2}\chi'(-c)\sum_{a\in\mathbf F_p}(\chi^{-1}\chi')(a) =\frac1p\delta_{\chi,\chi'}\chi(-c)$ by the orthogonality relation
[lem-fd-character-orthogonality]. Hence
$e_\chi e_{\chi'}=\delta_{\chi,\chi'}e_\chi$ and $\sum_\chi e_\chi=1$, so

$$
\pi_*\overline{\mathbf Q}_\ell=\bigoplus_{\chi\in\widehat{\mathbf F}_p}
\mathcal L_\chi,\qquad \mathcal L_\chi=e_\chi\,\pi_*\overline{\mathbf Q}_\ell ,
$$

a direct sum decomposition by idempotents, with no appeal to a splitting
theorem for group algebras.
*Step 4 (each summand is lisse of rank one; $\mathcal L_\chi=1$ iff
$\chi=0$).* Pulling $\mathcal L_\chi$ back along $\pi$ gives the constant
subsheaf $e_\chi\overline{\mathbf Q}_\ell[\mathbf F_p]$ of the regular
representation; the rank of an idempotent equals its trace, and
$\operatorname{tr}\sigma_a=p\delta_{a,0}$, so
$\operatorname{tr}e_\chi=\chi(0)=1$. Hence $\pi^*\mathcal L_\chi$ is constant
of rank one, and $\mathcal L_\chi$ is lisse of rank one by
[def-weil-pbc-etale-sheaves]. The summand $\chi=0$ is the invariant part
$(\pi_*\overline{\mathbf Q}_\ell)^{\mathbf F_p}$, i.e. the invariants of the
pushforward along a torsor, which is the constant sheaf
$\overline{\mathbf Q}_\ell$; so $\mathcal L_\chi=1$ if and only if $\chi=0$.
*Step 5 (multiplicativity).* Let $f,g\in\mathcal O_{X_0}$ with covers
$Y_f,Y_g$. Over the étale cover $Y_f\times_{X_0}Y_g\to X_0$ the two sheaves
$\mathcal L_{\psi,f}$ and $\mathcal L_{\psi,g}$ become constant of rank one
with the characters $\chi_f(a)=\psi(af)$ and $\chi_g(a)=\psi(ag)$ (Step 4),
and $T_f+T_g$ satisfies $(T_f+T_g)^p-(T_f+T_g)=f+g$, so the same
trivialization exhibits their tensor product as the constant sheaf with
character $\chi_f\chi_g=\chi_{f+g}$, namely the pullback of
$\mathcal L_{\psi,f+g}$. A morphism of sheaves on the étale site is an
isomorphism as soon as it becomes one after pullback along a cover, so
$\mathcal L_{\psi,f}\otimes\mathcal L_{\psi,g}\cong\mathcal L_{\psi,f+g}$;
the same argument with $g=-f$ gives
$(\mathcal L_{\psi,f})^{-1}\cong\mathcal L_{-\psi,f}$.
