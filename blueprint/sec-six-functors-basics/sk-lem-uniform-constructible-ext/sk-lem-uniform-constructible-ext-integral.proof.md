+++
kind = "proof"
of = "det-uniform-constructible-ext-integral"
+++
*Completeness of the target.* By parts (3) and (4) of [sk-lem-integral-models], $b_!M_0$ lies in
$\Dbc(X,\mathcal O_E)$, so it is derived complete. Since $b_!$ is exact and $M_0$ is $\pi_E$-torsion
free, $b_!M_0\otimes^{\mathbf L}\mathcal O_E/\pi_E^n=b_!(M_0/\pi_E^n)$; thus
$b_!M_0=R\varprojlim_nb_!(M_0/\pi_E^n)$.

*Completeness of $F$.* Put $F=L_0^\vee\otimes u^*R\underline\Gamma_Z\,b_!M_0$. By
[sk-lem-formal-closed-support-ii], each functor in this composite commutes with derived inverse limits
of sequences. Each also commutes with reduction modulo $\pi_E^n$, the cone of multiplication by
$\pi_E^n$, being exact and $\mathcal O_E$-linear. Hence

$$
F=R\varprojlim_nF_n,\qquad F_n=F\otimes^{\mathbf L}\mathcal O_E/\pi_E^n
=(L_0^\vee/\pi_E^n)\otimes u^*R\underline\Gamma_Z\,b_!(M_0/\pi_E^n).
$$

*Global sections.* $R\Gamma(S,-)$ is a right adjoint, so it preserves products, and it is exact, so it
preserves derived inverse limits of sequences. By part (2) of [sk-lem-formal-closed-support] (with
$\Lambda=\mathcal O_E$),

$$
R\operatorname{Hom}_X(a_!L_0,b_!M_0)=R\Gamma(S,F)=R\varprojlim_nR\Gamma(S,F_n).
$$

*The bound.* Put $c=\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+1$. By
[det-uniform-constructible-ext-torsion], $H^qR\Gamma(S,F_n)=0$ for $q>c$. The Milnor sequence

$$
0\to\varprojlim^1_nH^{q-1}R\Gamma(S,F_n)\to H^qR\varprojlim_nR\Gamma(S,F_n)\to\varprojlim_nH^qR\Gamma(S,F_n)\to0
$$

(the derived limit is the fiber of $1-\mathrm{shift}$ on a product, and products of abelian groups are
exact; Stacks, Tag 08TB) shows that $H^q$ of the limit vanishes as soon as $q>c$ and $q-1>c$, i.e. for
$q>c+1$. This is the claim.
