+++
kind  = "proof"
of    = "prop-trf-trace-class-additivity"
+++
The first assertion of (1) is exactly
[lem-trf-trace-triangle-compatibility]. For the second, suppose
$F$ proper over $s$ with finitely many open-and-closed components
$\beta\in\pi_0(F)$; the local terms of
[def-trf-local-term] are the integrals
$\operatorname{LT}_\beta(u)=\int_\beta\operatorname{Tr}_c(u)|_\beta$
of [def-trf-integration], and integration is $A$-linear by
[lem-trf-integration-linear], so
additivity of the classes gives
$\operatorname{LT}_\beta(u)=\operatorname{LT}_\beta(u')+ \operatorname{LT}_\beta(u'')$ for every $\beta$.

For (2), write $\Phi=\Phi_m$ and let
$$
K^U\xrightarrow{\ \varepsilon\ }K\xrightarrow{\ \eta\ }K^Z
\xrightarrow{\ \delta\ }K^U[1]
$$
be the open–closed triangle of [prop-sf-open-closed-triangle-all-stages],
with $\varepsilon$ the counit of $j_!\dashv j^*$ and $\eta$ the unit of
$i^*\dashv Ri_*$. The functor $L\Phi^*$ is exact, so it carries this
triangle to a distinguished triangle, and $Rc_1^!=\operatorname{id}$.
Let $b:L\Phi^*j_!\xrightarrow{\sim}j_!L\Phi_U^*$ be the open base-change
isomorphism used in $u^U$ ([prop-functor-package], clause (4)), and
$\gamma$ the ordinary half used in $u^Z$, as in [d-curve-pieces].

(a) $\varepsilon\circ u^U=v\circ L\Phi^*\varepsilon$. By the adjunction
$j_!\dashv j^*$ of [prop-weil-open-closed-recollement-adjunctions] it
suffices to compare the restrictions to $U$ of the two maps
$L\Phi^*j_!j^*K\cong j_!L\Phi_U^*j^*K\to K$. There $b$ restricts to the
pullback identification and $j^*\varepsilon$ to the identity, so both
restrictions equal $j^*v$ composed with
$L\Phi_U^*j^*\cong j^*L\Phi^*$.

(b) $u^Z\circ L\Phi^*\eta=\eta\circ v$. By the adjunction $i^*\dashv Ri_*$
it suffices to compare the adjoint maps $i^*L\Phi^*K\to i^*K$. The
adjoint of $\eta\circ v$ is $i^*v$. By the construction of $\gamma$ as
unit followed by counit, the triangle identities make the adjoint of
$u^Z\circ L\Phi^*\eta=Ri_*v_{\bar x}\circ\gamma\circ L\Phi^*\eta$
equal to $v_{\bar x}$ precomposed with $i^*L\Phi^*K\cong(\Phi i)^*K=i^*K$;
this is $i^*v$, by the definition of the stalk map $v_{\bar x}$
($i^*$ being the stalk at $\bar x$).

(c) $u^U[1]\circ L\Phi^*\delta=\delta\circ u^Z$. By (a), (b) and the
axiom of morphisms of triangles there is
$w:L\Phi^*K^Z\to K^Z$ with $w\circ L\Phi^*\eta=\eta\circ v$ and
$\delta\circ w=u^U[1]\circ L\Phi^*\delta$. Then
$(w-u^Z)\circ L\Phi^*\eta=0$, so $w-u^Z$ factors through
$L\Phi^*\delta$ as $d\circ L\Phi^*\delta$ with
$d:L\Phi^*K^U[1]\to K^Z$. Via $b$ the source of $d$ is
$j_!N[1]$ with $N=L\Phi_U^*j^*K$, and
$\operatorname{Hom}(j_!N[1],Ri_*i^*K)=\operatorname{Hom}(N[1],j^*Ri_*i^*K)=0$
because $j^*Ri_*=0$ ([prop-weil-open-closed-recollement-adjunctions],
as in the Hom vanishing of [prop-sf-open-closed-triangle-all-stages]).
Hence $w=u^Z$.

Thus $(u^U,v,u^Z)$ is the induced morphism of the open–closed triangles
for the closed point $Z=\{\bar x\}$, which is $c$-invariant because
$c_1=\operatorname{id}$ and $\Phi(\bar x)=\bar x$, and $u^U,u^Z$ are the
induced coefficient morphisms $[j]_!(v|_U)$, $[i]_!(v|_Z)$ of
[lem-trf-trace-triangle-compatibility]; so (1) gives the identity of trace
classes. The fixed scheme $F=\operatorname{Fix}(\Phi)$
is a finite disjoint union of copies of $\operatorname{Spec}k$ by
[thm-trf-frobenius-fixed-points], hence proper over $s$ with finitely
many open-and-closed components, so (1) also gives the identity of local
terms. No step inverts $v$.
