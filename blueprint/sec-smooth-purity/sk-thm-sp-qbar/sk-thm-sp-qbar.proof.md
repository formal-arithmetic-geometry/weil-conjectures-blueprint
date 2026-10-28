+++
kind = "proof"
of = "sk-thm-sp-qbar"
uses = ["sk-prop-qlbar-two-colimit", "sk-prop-sp-rational", "sk-lem-sp-field-extension", "sk-prop-sf-comp-coherence"]
+++
By [sk-prop-qlbar-two-colimit], $\Dbc(T,\Qlb)$ is the $2$-colimit of the
categories $\Dbc(T,E)$; in particular, for $K,L\in\Dbc(T,E)$,
$\varinjlim_{F\supset E}\Hom(K_F,L_F[q])\xrightarrow{\sim}\Hom(K_{\Qlb},L_{\Qlb}[q])$,
with Hom groups in $\Dbc(T,F)$ and $\Dbc(T,\Qlb)$. Hence any finite diagram of
$\Qlb$-complexes, with finitely many relations, is defined over one finite
extension of $\Ql$. The functors $Rf_{!,\Qlb}$ and $f^*_{\Qlb}$ commute with
extension of scalars from $E$, and $Rf_{!,\Qlb}$ is independent of the
compactification by [sk-prop-sf-comp-coherence].

Choose models $M_E,K_E$ over one finite $E$. By the compatibility with
extension of scalars, the colimit formula for Hom groups and
[sk-prop-sp-rational] over each $F\supset E$,

$$
\begin{aligned}
\operatorname{Hom}(Rf_{!,\Qlb}M,K)
&\simeq\varinjlim_{F}\operatorname{Hom}\bigl(Rf_{!,F}M_F,K_F\bigr)\\
&\simeq\varinjlim_{F}\operatorname{Hom}\bigl(M_F,f_F^*K_F(d)[2d]\bigr)
\simeq\operatorname{Hom}(M,f_{\Qlb}^*K(d)[2d]),
\end{aligned}
$$

with Hom groups in $\Dbc(Y,\Qlb)$, $\Dbc(Y,F)$, $\Dbc(X,F)$ and $\Dbc(X,\Qlb)$.
The middle bijections are given by $\eta_{f,F}$ and $\varepsilon_{f,F}$, which
are compatible with the transition maps by [sk-lem-sp-field-extension]. The
bijection is independent of the models and natural, because the isomorphisms,
morphisms and relations involved are defined over one finite $F$, where the
adjunction is natural.
