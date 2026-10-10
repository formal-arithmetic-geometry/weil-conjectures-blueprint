+++
kind  = "proof"
of    = "thm-trf-frobenius-local-term"
+++
The proof follows the curve pieces of [d-curve-pieces]. Fix
$y\in X_0(\mathbf F_{q^m})$, put $x=y$, $\Phi=\Phi^m$, and let $v$ be
$u_m$ or an arbitrary morphism $L\Phi^*K\to K$ as in the statement. All
morphisms below are separated and of finite type between separated
finite-type $k$-schemes, hence exceptionally admissible at the finite
stage ([rem-ptr-trf-admissibility-12], [thm-sf-preservation-class]).

*Step 0: the fixed point.* By [thm-trf-frobenius-fixed-points] the
fixed scheme $\operatorname{Fix}(\Phi)$ is a finite disjoint union of
copies of $\operatorname{Spec}k$, one for each point of
$X_0(\mathbf F_{q^m})$. So it is proper over $s$ with finitely many
open-and-closed components, the geometric point $\bar x$ is one of them,
a reduced point component, and $\operatorname{LT}_{\bar x}$ is the local
term of [def-trf-local-term] computed as in [lem-trf-local-term-point].

*Step 1: the pieces.* Let $i:\{\bar x\}\hookrightarrow X$,
$j:U=X\setminus\{\bar x\}\hookrightarrow X$, and let
$K^Z=Ri_*i^*K$, $K^U=j_!j^*K$ with the induced maps $u^Z,u^U$ of
[d-curve-pieces] for the coefficient morphism $v$. By
[prop-trf-trace-class-additivity], item (2),

$$
\operatorname{LT}_{\bar x}(v)=\operatorname{LT}_{\bar x}(u^Z)
+\operatorname{LT}_{\bar x}(u^U).
$$

*Step 2: the open piece.* The stalk of the extension by zero at the
point $\bar x\notin U$ vanishes, $(K^U)_{\bar x}=(j_!j^*K)_{\bar x}=0$
([def-weil-extension-by-zero]). The map
$u^U:L\Phi^*K^U\to K^U$ is a Frobenius coefficient morphism for
$\Phi=\Phi^m$ on $K^U$, and it is not required to be invertible.
Hence $\operatorname{LT}_{\bar x}(u^U)=0$ by the zero-stalk vanishing
of [lem-trf-local-term-locality]: item (3) in the smooth-curve setting
of [d-curve-pieces], and item (2) for general $X_0$, the graph of $\Phi$
being contracting at $\bar x$ because
$\Phi^{\cdot}(\mathcal I_{\bar x})\mathcal O_X\subset\mathcal I_{\bar x}^{\,q^m}$
(verified in the proof of item (3) there). This is the only step of the
proof that is not formal: it rests on Varshavsky's
contracting-correspondence theorem, quoted in that lemma.

*Step 3: the closed piece.* By [d-curve-pieces],
$u^Z=[i,i]_!(v_{\bar x})$ is the coefficient pushforward of
[def-trf-coefficient-pushforward] along the proper pushforward diagram
$(i,i)$ from the point correspondence
$c_{\mathrm{pt}}=(\operatorname{id},\operatorname{id})$ on
$\operatorname{Spec}k$, with coefficient $v_{\bar x}$ on $K_{\bar x}$, to
the graph $c=(\operatorname{id}_X,\Phi)$; the closed immersion $i$ is
proper. The fixed scheme of $c_{\mathrm{pt}}$ is $\operatorname{Spec}k$,
and the induced map of fixed schemes
$h:\operatorname{Spec}k\to\operatorname{Fix}(\Phi)$ is the inclusion of
the component $\bar x$. The proper pushforward compatibility
[thm-trf-trace-proper-compatibility] gives

$$
\operatorname{Tr}_c(u^Z)=h_*\operatorname{Tr}_{c_{\mathrm{pt}}}(v_{\bar x})
$$

with $h_*$ the Borel–Moore pushforward of
[def-trf-borel-moore-pushforward]. Since $h$ is an open-and-closed
immersion, $Lh^*Rh_*\cong\operatorname{id}$ and, by the triangle
identities, the unit $\eta_h$ and the counit $\varepsilon_h$ in the
definition of $h_*$ restrict to identities along $h$. Hence
$\operatorname{Tr}_c(u^Z)|_{\bar x}=\operatorname{Tr}_{c_{\mathrm{pt}}}(v_{\bar x})$
and

$$
\operatorname{LT}_{\bar x}(u^Z)
=\int_{\operatorname{Spec}k}\operatorname{Tr}_{c_{\mathrm{pt}}}(v_{\bar x})
=\operatorname{LT}_s(v_{\bar x})
=\operatorname{tr}_A\bigl(v_{\bar x}\mid K_{\bar x}\bigr)
$$

by the point normalization of [prop-trf-pairing-local-decomposition],
the stalk $K_{\bar x}$ being perfect by [fix-lem-finite-tor-perfect].

*Step 4: conclusion.* Steps 1–3 give
$\operatorname{LT}_{\bar x}(v)=\operatorname{tr}_A(v_{\bar x}\mid K_{\bar x})$.
For $v=u_m$ the stalk map $u_{m,\bar x}$ is the local geometric
Frobenius $F_{x,m}$ of [def-trf-frobenius-operators], as recorded in
[d-curve-pieces], which proves the first formula. No step inverts $v$.
