+++
kind  = "proof"
of    = "prop-trf-graph-frobenius-operator"
+++
By [prop-trf-graph-operator] applied to $h=\Phi^m$ (finite,
hence proper, by [def-trf-scheme-frobenius]) and to $v=u_m$,
the operator $T_c(u_m)$ is the composite

$$
R\Gamma_c(X,K)\xrightarrow{\ \eta_{\Phi^m}\ }
R\Gamma_c(X,L\Phi^{m*}K)\xrightarrow{R\Gamma_c(X,u_m)}R\Gamma_c(X,K),
$$

where $\eta_{\Phi^m}$ is the unit of
$L\Phi^{m*}\dashv R\Phi^{m}_*$ composed with the identification
$R\Phi^{m}_*\cong R\Phi^{m}_!$ and the composition law for the
compact-support direct image ([def-trf-global-operator],
[prop-trf-graph-operator], [prop-functor-package],
item (3)).

*Step 1: the identification of the functors and of the units.*
As $L\Phi^{m*}$ and $Lg_\gamma^{m*}$ are left adjoints to
$R\Phi^{m}_*$ and $Rg_\gamma^{m,*}$, respectively, with the
adjunction data of (the derived direct image of)
[prop-functor-package], and as
[prop-trf-scheme-galois-comparison] supplies the natural isomorphism

$$
\kappa^{(m)}:L\Phi^{m*}\xrightarrow{\ \sim\ }Lg_\gamma^{m*},
$$

the mate lemma [lem-trf-adjoint-mate] supplies the canonical
natural isomorphism

$$
\beta:R\Phi^{m}_*\xrightarrow{\ \sim\ }Rg_\gamma^{m,*}
$$

(unique subject to the unit and counit compatibilities, by (3) of
[lem-trf-adjoint-mate]), together with the unit compatibility
in the form

$$
Rg_\gamma^{m,*}\kappa^{(m)}\circ\beta L\Phi^{m*}\circ\eta_{\Phi^m}
=\eta_{\gamma^m},
$$

where $\eta_{\gamma^m}$ is the unit of
$Lg_\gamma^{m*}\dashv Rg_\gamma^{m,*}$. Hence the *transported
unit* of $T_c(u_m)$ is the geometric-Frobenius unit, and the diagram

$$
\begin{array}{ccc}
R\Gamma_c(X,K) & \xrightarrow{\ \eta_{\Phi^m}\ }
& R\Gamma_c(X,L\Phi^{m*}K)\\
& & \ \ \downarrow{\scriptstyle R\Gamma_c(X,\kappa^{(m)})}\\
& & R\Gamma_c(X,Lg_\gamma^{m*}K)
\end{array}
$$

commutes with the corresponding composite starting from
$\eta_{\gamma^m}$ after the identification of the targets along
$R\Gamma_c(X,R\Phi^{m}_*L\Phi^{m*}K)\cong R\Gamma_c(X,Rg_\gamma^{m,*}Lg_\gamma^{m*}K)$ supplied by $\beta$.

*Step 2: identification with the compact-support base change.*
The composite

$$
R\Gamma_c(X,K)\xrightarrow{\ \eta_{\gamma^m}\ }
R\Gamma_c(X,Rg_\gamma^{m,*}Lg_\gamma^{m*}K)
\xrightarrow{\ \sim\ }R\Gamma_c(X,Lg_\gamma^{m*}K)
$$

(the identification $Rg_\gamma^{m,*}\cong Rg_\gamma^{m,!}$ for the
proper, indeed finite, automorphism $g_\gamma^m$ together with the
compact-support composition law) is, by the construction of
[def-weil-global-geometric-frobenius], the first arrow of the
compact-support base-change identification $g_{\gamma,c}^{m,*}$
(the exchange $\operatorname{Ex}_!$ of
[def-exchange-projection] along the automorphism $g_\gamma^m$,
composed with the canonical identification of the compact-support
cohomology of an isomorphism-fixed scheme and the naturality of
$R\Gamma_c$); and the compatibility of this exchange with the
adjunction data and with the identifications of Step 1 is part of the
adjunction-compatibility and coherence records of the package
([def-exchange-projection] and [prop-functor-package]).
Therefore the first arrow of the composite defining $T_c(u_m)$ equals
the arrow $g_{\gamma,c}^{m,*}$, and the last arrow is
$R\Gamma_c(X,\varphi^{[m]})\circ R\Gamma_c(X,\kappa^{(m)})$,
whence

$$
T_c(u_m)=R\Gamma_c(X,\varphi^{[m]})\circ g_{\gamma,c}^{m,*}
=F_{c,K}^{\,m}
$$

by [lem-trf-frobenius-operator-compact-description], where
$F_{c,K}^{\,m}$ is the $m$-th iterate of the global geometric
Frobenius of [def-trf-frobenius-operators] and
$\varphi^{[m]}$ is the iterated Weil isomorphism of
[def-trf-iterated-weil-map]. Naturality in $(K,\varphi)$ is
the naturality of $\kappa^{(m)}$ of [prop-trf-scheme-galois-comparison]
and of the base-change identification. The compatibility with the
cocycle law in $m$: for $m,n\geq1$, the base-change identifications
along the automorphisms compose as

$$
g_{\gamma,c}^{m+n,*}
=\bigl(g_{\gamma,c}^{m,*}\bigr)_{Lg_\gamma^{n*}K}\circ g_{\gamma,c}^{n,*}
$$

(transitivity of the compact-support base change, from
$g_\gamma^{m+n}=g_\gamma^m\circ g_\gamma^n$), and the base-change
identification is natural in the coefficient complex, so by the cocycle
identity $\varphi^{[m+n]}=\varphi^{[m]}\circ Lg_\gamma^{m*}\varphi^{[n]}$
of [lem-trf-iterated-weil-cocycle] one has

$$
\begin{aligned}
F_{c,K}^{\,m+n}
&=R\Gamma_c(X,\varphi^{[m+n]})\circ g_{\gamma,c}^{m+n,*}\\
&=R\Gamma_c(X,\varphi^{[m]})\circ R\Gamma_c(X,Lg_\gamma^{m*}\varphi^{[n]})
\circ\bigl(g_{\gamma,c}^{m,*}\bigr)_{Lg_\gamma^{n*}K}\circ g_{\gamma,c}^{n,*}\\
&=R\Gamma_c(X,\varphi^{[m]})\circ g_{\gamma,c}^{m,*}
\circ R\Gamma_c(X,\varphi^{[n]})\circ g_{\gamma,c}^{n,*}
=F_{c,K}^{\,m}\circ F_{c,K}^{\,n},
\end{aligned}
$$

which is the claimed cocycle compatibility (the third equality uses the
naturality of $g^{m,*}$ in the coefficient complex; multiplicativity of
the $\kappa^{(m)\,}$s of [prop-trf-scheme-galois-comparison]
transports the same identity to the scheme-Frobenius side).

*Step 3: general coefficient maps.* Steps 1 and 2 concern only the
object $K$ and the functors $L\Phi^{m*}$, $Lg_\gamma^{m*}$, $R\Gamma_c$:
neither the Weil structure $\varphi$ nor any inverse of a coefficient map
enters them. For an arbitrary $K\in D^b_{ctf}(X,A)$ they give that the
composite

$$
R\Gamma_c(X,K)\xrightarrow{\ \eta_{\Phi^m}\ }R\Gamma_c(X,L\Phi^{m*}K)
\xrightarrow{R\Gamma_c(X,\kappa^{(m)}_K)}R\Gamma_c(X,Lg_\gamma^{m*}K)
$$

is $g_{\gamma,c}^{m,*}$. For $v:Lg_\gamma^{m*}K\to K$ arbitrary,
[prop-trf-graph-operator] applied to $h=\Phi^m$ and to the coefficient
map $v\circ\kappa^{(m)}_K$, together with functoriality of
$R\Gamma_c(X,-)$, gives

$$
T_c\bigl(v\circ\kappa^{(m)}_K\bigr)
=R\Gamma_c(X,v)\circ R\Gamma_c(X,\kappa^{(m)}_K)\circ\eta_{\Phi^m}
=R\Gamma_c(X,v)\circ g_{\gamma,c}^{m,*},
$$

which is the general assertion; for $v=\varphi^{[m]}$ it is the identity
$T_c(u_m)=F_{c,K}^{\,m}$ proved above.
