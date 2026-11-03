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
Write $g=g_\gamma^m$, $Rg_*=Rg_\gamma^{m,*}$, $\kappa=\kappa^{(m)}$,
$\gamma_s=\operatorname{Spec}(\gamma):s\to s$ and
$C=R\Gamma_c(X,-)=\operatorname{Fib}_sRa_{X!}$. Let

$$
\iota_\Phi:CR\Phi^m_*\xrightarrow{\ \sim\ }C,
\qquad
\iota_g:CRg_*\xrightarrow{\ \sim\ }C
$$

be the actual compact-support identifications: $\iota_\Phi$ is
$\operatorname{Fib}_s$ of
$Ra_{X!}R\Phi^m_*\cong Ra_{X!}R\Phi^m_!\cong R(a_X\Phi^m)_!=Ra_{X!}$
($\Phi^m$ is a finite $k$-morphism, so $a_X\Phi^m=a_X$), and $\iota_g$ is
the middle identification of [def-weil-global-geometric-frobenius] for
$g$, which uses the semilinear relation $a_Xg=\gamma_s^ma_X$, followed by
$\lambda_{\gamma^m}:\operatorname{Fib}_sR\gamma^m_{s!}\cong\operatorname{Fib}_s$.
Thus the first arrow of $T_c(u_m)$ is
$u_{\Phi^m,!}(K)=\iota_\Phi\circ C(\eta_{\Phi^m,K})$, and by
[def-weil-global-geometric-frobenius] the compact-support base-change
isomorphism is its first arrow

$$
g_{\gamma,c}^{m,*}=u_{g,!}(K)=\iota_g\circ C(\eta_{\gamma^m,K}):
R\Gamma_c(X,K)\xrightarrow{\ \sim\ }R\Gamma_c(X,Lg_\gamma^{m*}K).
$$

No description of $g_{\gamma,c}^{m,*}$ as an exchange map is used here.
Consumers that use the exchange form need a separate exchange-comparison
lemma identifying $u_{g,!}$ with $\operatorname{Fib}_s$ of the exchange
along $g$ (after $\operatorname{Fib}_s\cong\operatorname{Fib}_sL\gamma_s^{m*}$). This
lemma needs an isomorphism-square companion to [def-exchange-projection], or a
formulation using the twisted $k$-structure on the source, because the
finite-type $S$-linear conventions of [def-exchange-projection] do not
literally cover the semilinear square $a_Xg=\gamma_s^ma_X$.

The required compatibility is

$$
\iota_g\circ C(\beta)=\iota_\Phi:\ CR\Phi^m_*\longrightarrow C.
\qquad(*)
$$

Granting $(*)$, the unit compatibility of Step 1 and the naturality of
$\iota_g$ give

$$
u_{g,!}(K)=\iota_g\circ C(Rg_*\kappa_K)\circ C(\beta_{L\Phi^{m*}K})\circ C(\eta_{\Phi^m,K})
=C(\kappa_K)\circ\iota_g\circ C(\beta)\circ C(\eta_{\Phi^m,K})
=C(\kappa_K)\circ u_{\Phi^m,!}(K).
$$

A generic mate-unit identity does not prove $(*)$. Both $\iota$'s are
fixed compact-support identifications, so $(*)$ depends on $\kappa$ being
the specified comparison of [prop-trf-scheme-galois-comparison]. That
comparison is built from the normalized trivialization of the
absolute-Frobenius pullback ([lem-trf-absolute-frobenius-site]) through the
factorization [prop-trf-frobenius-factorization]. Prove $(*)$ over a
compactification descended from $X_0$. Choose $X_0\hookrightarrow\bar X_0$
over $k_0$ ([lem-sfb-compactification-over-base]) and base change it to
$X\xrightarrow{j}\bar X\xrightarrow{\bar a}s$
([def-weil-compactifications-refinements]).
(a) *Extend the maps.* $\bar\Phi=\bar\Phi_0^m\times\operatorname{id}_k$ and
$\bar g=\operatorname{id}_{\bar X_0}\times\gamma_s^m$ satisfy $\bar\Phi j=j\Phi^m$,
$\bar gj=jg$, $\bar\Phi^{-1}(X)=\bar g^{-1}(X)=X$, $\bar a\bar\Phi=\bar a$ and
$\bar a\bar g=\gamma_s^m\bar a$. The factorization of the absolute $q^m$-power
Frobenius holds on $\bar X$ compatibly with $j$. The same recipe gives
$\bar\kappa:L\bar\Phi^*\cong L\bar g^*$ and its mate $\bar\beta$, and
$j^*\bar\kappa=\kappa j^*$ because the site trivialization commutes with
restriction to opens.
(b) *Check against $j_!$.* $R\bar\Phi_*j_!\cong j_!R\Phi^m_*$ and
$R\bar g_*j_!\cong j_!Rg_*$. Under these, $\bar\beta_{j_!M}=j_!\beta_M$:
both are maps between extensions by zero [def-weil-extension-by-zero]
restricting to $\beta_M$ on $X$, and $j_!$ is fully faithful.
(c) *Check against direct image.* On $\bar X$, $\iota_\Phi$ and $\iota_g$
are $\operatorname{Fib}_s$ of $R\bar a_*R\bar\Phi_*\cong R(\bar a\bar\Phi)_*=R\bar a_*$
and of $R\bar a_*R\bar g_*\cong R\gamma^m_{s*}R\bar a_*$ followed by
$\lambda_{\gamma^m}$ ([def-weil-global-geometric-frobenius],
[prop-compactification-coherence-detailed]). The absolute Frobenius
commutes with $\bar a$, and the canonical trivialization is compatible with
$R\bar a_*$. On $s$, where the absolute $q^m$-power Frobenius is
$\operatorname{Spec}(\sigma^m)=\gamma_s^{-m}$, its normalized trivialization,
evaluated by $\operatorname{Fib}_s$, is the coefficient-section
identification $\lambda$.
(d) *Derive the diagram.* By (a) and (c), $\iota_{\bar g}\circ C(\bar\beta)=\iota_{\bar\Phi}$
on $\bar X$. Evaluating this identity at $j_!L$ for $L$ on $X$, and using (b) with $M=L$, gives $(*)$.
These comparisons, and the iteration below, use only the site invariance
of the absolute Frobenius and compactification coherence. They precede
the trace formula and use neither purity nor Verdier duality.
Since $u_m=\varphi^{[m]}\circ\kappa^{(m)}_K$ ([def-trf-iterated-weil-map]),
the composite defining $T_c(u_m)$ is
$R\Gamma_c(X,\varphi^{[m]})\circ R\Gamma_c(X,\kappa^{(m)})\circ u_{\Phi^m,!}(K)
=R\Gamma_c(X,\varphi^{[m]})\circ g_{\gamma,c}^{m,*}$,
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

(from $g_\gamma^{m+n}=g_\gamma^n\circ g_\gamma^m$: put $L_1=Lg_\gamma^{n*}$,
$R_1=Rg_\gamma^{n,*}$, $L_2=Lg_\gamma^{m*}$, $R_2=Rg_\gamma^{m,*}$. The unit of the
composite adjunction $L_2L_1\dashv R_1R_2$ is the whiskered composite
$\eta_{L_2L_1}=(R_1\eta_2L_1)\circ\eta_1$, and under the pullback and
direct-image compositors it is the unit $\eta_{\gamma^{m+n}}$. The
compositor coherence of the compact-support identifications
([prop-functor-package], item (3)) and the composition coherence
$\lambda_{\gamma^{m+n}}=\lambda_{\gamma^n}\circ(\lambda_{\gamma^m})_{R\gamma^n_{s*}}\circ\operatorname{Fib}_s(c)$
of [def-weil-global-geometric-frobenius] then give
$\iota_{g^{m+n}}=\iota_{g^n}\circ(\iota_{g^m})_{Rg^n_*}\circ C(c)$. Applying
the definition $u_{g,!}=\iota_g\circ C(\eta)$ yields the displayed
transitivity), and the base-change
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
