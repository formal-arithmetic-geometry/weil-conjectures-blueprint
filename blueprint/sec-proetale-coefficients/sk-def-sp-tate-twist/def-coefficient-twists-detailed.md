+++
id = "def-coefficient-twists-detailed"
kind = "definition"
title = "Coefficient Tate twists"
order = 1864
uses = ["sk-def-sp-tate-twist", "sk-def-sfb-pulled-back-coefficients", "sk-prop-sfb-qlbar-colimit-x", "def-weil-derived-tensor", "def-weil-pbc-proetale-site"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$ with uniformizer $\pi_E$, an
integer $n\in\mathbf Z_{\geq1}$, and a scheme $S$ on which $\ell$ is
invertible. Use the small pro-étale site [def-weil-pbc-proetale-site] of $S$
and the derived tensor product [def-weil-derived-tensor]. For every integer
$r\geq1$, define the pro-étale sheaf $\mu_{\ell^r,S}$ by

$$
 \mu_{\ell^r,S}(U)=
 \{u\in\Gamma(U,\mathcal O_U^\times):u^{\ell^r}=1\}
 \qquad(U\to S).
$$

For every coefficient ring
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, with $A_{E,n}=\mathcal O_E/\pi_E^n$,
the coefficient sheaf is the pulled-back condensed ring
$\Lambda_S=p_S^*\Lambda$ of [sk-def-sfb-pulled-back-coefficients]. The twists
$\Lambda(1)_S$ are those of [sk-def-sp-tate-twist]:

$$
 A_{E,n}(1)_S=\mu_{\ell^r,S}\otimes_{\mathbf Z/\ell^r\mathbf Z}(A_{E,n})_S
 \quad(\ell^rA_{E,n}=0),
 \qquad
 \mathcal O_E(1)_S=\varprojlim_n A_{E,n}(1)_S,
$$

the first independent of $r$ by the Kummer maps $u\mapsto u^\ell$, and

$$
 E(1)_S=\mathcal O_E(1)_S\otimes_{\mathcal O_{E,S}}E_S,
 \qquad
 \Qlb(1)_S=\operatorname*{colim}_{E}E(1)_S,
$$

using $E_S=\mathcal O_{E,S}[1/\ell]$ and
$\overline{\mathbf Q}_{\ell,S}=\operatorname{colim}_EE_S$ from
[sk-prop-sfb-qlbar-colimit-x]. Each $\Lambda(1)_S$ is an invertible
$\Lambda_S$-module, locally isomorphic to $\Lambda_S$. Define the twist for
every $m\in\mathbf Z$ by

$$
 \Lambda(m):=
 \begin{cases}
   \Lambda_S,&m=0,\\
   \Lambda(1)_S^{\otimes_{\Lambda_S}m},&m>0,\\
   \operatorname{Hom}_{\Lambda_S}\bigl(\Lambda(-m),\Lambda_S\bigr),&m<0.
 \end{cases}
$$

For every $m\in\mathbf Z$ and every $K\in D(S_{\mathrm{proét}},\Lambda)$, set

$$
 K(m)=K\otimes^L_{\Lambda_S}\Lambda(m).
$$
