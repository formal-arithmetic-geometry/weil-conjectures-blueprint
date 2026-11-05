+++
kind = "proof"
of = "det-proper-heart-bound-torsion"
+++
*Reduction.* $L_0$ is flat over $\mathcal O_{E,S}$, so $L_0\otimes^{\mathbf L}\mathcal O_E/\pi_E^n=L_0/\pi_E^n$, and $a_!$
is exact, so it commutes with the cone of $\pi_E^n$; hence the derived reduction of $a_!L_0$ is the sheaf
$a_!(L_0/\pi_E^n)$. The lisse torsion sheaf $L_0/\pi_E^n$ is pulled back from $S_{\mathrm{ét}}$ ([Stacks, Tag 099Y](https://stacks.math.columbia.edu/tag/099Y)), and $a_!$ commutes with that pullback (Stacks, Tags 09AF, 09A6), so $a_!(L_0/\pi_E^n)=\nu^*F$ for a
constructible étale sheaf $F$ of $\mathcal O_E/\pi_E^n$-modules on $X$.

*Étale vanishing.* $p_V$ is proper with geometric fibres of dimension $\leq d$ (base change does not
change geometric fibres). By the proper vanishing theorem ([Stacks, Tag 095U](https://stacks.math.columbia.edu/tag/095U)), valid over any base and in
particular over the non-Noetherian $V$, $R^qp_{V,*}F|_{X_V}=0$ for $q>2d$ on the étale site.

*Comparison.* By Stacks, Tag 09A6, the pro-étale $Rp_{V,*}$ of $\nu^*F$ is $\nu^*$ of the étale
$Rp_{V,*}F$; so $R^qp_{V,*}(a_!(L_0/\pi_E^n)|_{X_V})=0$ for $q>2d$.

*Sections.* Since $V$ is weakly contractible, $\Gamma(V,-)$ is exact on all pro-étale sheaves
([sk-cor-pe-wc-sections]; Stacks, Tag 0991), so $R\Gamma(X_V,-)=\Gamma(V,Rp_{V,*}(-))$ and
$H^q(X_V,-)=\Gamma(V,R^qp_{V,*}(-))$, which vanishes for $q>2d$.
