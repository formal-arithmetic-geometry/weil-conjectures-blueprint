+++
kind  = "proof"
of    = "prop-cohomological-finiteness"
+++
*Step 1 (finiteness).* Write $a_Y:Y\to s=\Spec k$ for the
structure morphism, a separated morphism of finite type
([def-weil-scheme-morphism-properties]) over the algebraically closed field
$k$, with $e=\dim Y$. By [sk-lem-finite], applied to the admissible
coefficient ring $E$ and $K\in\Dbc(Y,E)=\Dctf(Y,E)$, the complexes
$R\Gamma(Y,K)=Ra_{Y*}K$ and $R\Gamma_c(Y,K)=Ra_{Y!}K$ are perfect complexes
over the field $E$. Hence their cohomology groups are finite-dimensional and
vanish outside a finite interval; by its complement, if the cohomology
sheaves of $K$ lie in $[a,b]$, both vanish outside $[a,b+2e]$.

*Step 2 (Frobenius).* The Weil structure $\theta:Lg_Y^*K\to K$ of
[def-weil-weil-sheaf-complex], transported along the functoriality of the
direct images, gives the geometric-Frobenius automorphism of
[def-weil-global-geometric-frobenius] on the ordinary and on the
compact-support groups, as asserted.

*Step 3 (the proper case).* If $Y_0$ is proper, then
$a_Y$ is proper and the canonical comparison
$R\Gamma_c(Y,K)\to R\Gamma(Y,K)$ of
[def-weil-ordinary-compact-cohomology] is an isomorphism; it is
Frobenius-equivariant because both operators are those of Step 2.

*Step 4 (the constant sheaf).* For $K=E_Y$, placed in degree zero, Step 1
gives $H^i_c(Y,E)=0$ and $H^i(Y,E)=0$ for $i\notin[0,2e]$, and in the proper
case Step 3 identifies the two. The specialisation $Y=X$, $e=d$, $E=\Ql$ is
the vanishing $H^i(X,\Ql)=0$ for $i\notin[0,2d]$.

Finally let $Y_0$ be geometrically connected, so that $Y$ is connected. By
[sk-prop-sfb-qlbar-colimit-x], $\mathcal O_{E,Y}\cong\varprojlim_n(\mathcal
O_E/\pi_E^n)_Y$ and $E_Y\cong\mathcal O_{E,Y}[1/\ell]$. Global sections commute
with limits of sheaves, and, $Y$ being quasi-compact and quasi-separated,
with the filtered colimit defining $[1/\ell]$
([det-lem-coefficient-finite-descent-sections]). Since $Y$ is connected,
$H^0(Y,(\mathcal O_E/\pi_E^n)_Y)=\mathcal O_E/\pi_E^n$, so

$$
H^0(Y,E)=\Bigl(\varprojlim_n\mathcal O_E/\pi_E^n\Bigr)[1/\ell]=E .
$$

The geometric Frobenius acts as the identity on this group, since the Weil
structure of the constant Weil sheaf is the canonical identification
$g_Y^*E_Y\cong E_Y$, which is the identity on global constants
([def-weil-weil-sheaf-complex]). This argument uses only the connectedness of
$Y$, not properness or smoothness; the case $Y_0=X_0$, $E=\Ql$ gives
$H^0(X,\Ql)\cong\Ql$.
