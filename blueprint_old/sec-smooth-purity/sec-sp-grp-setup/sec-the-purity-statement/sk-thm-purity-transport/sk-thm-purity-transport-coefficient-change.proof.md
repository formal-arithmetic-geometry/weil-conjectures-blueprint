+++
kind = "proof"
of = "det-sp-purity-coefficient-change"
+++
In each case the argument has the same shape. The counit of the purity
adjunction $Rf_!\dashv f^*(-)(d)[2d]$, obtained by transporting $\varepsilon_f$
along $\gamma_f$, is the smooth trace ([det-sp-trace-basic], (1)). Since
$\gamma_f$ is the unique counit-compatible isomorphism, a statement about
$\gamma$ follows from the corresponding statement about counits by
transposition.

(1) By construction ([sk-prop-sp-integral-adjunction],
[det-sp-integral-adjunction-bijection]), $f^!_{\mathcal O_E}K$ is identified,
compatibly with counits, with $H_{f,\mathcal O_E}(K)=R\varprojlim_nf^!_\bullet(\operatorname{red}_YK)$.
The counit of $Rf_{!,\mathcal O_E}\dashv H_{f,\mathcal O_E}$ is the derived limit of the
tower counit, whose level $n$ is the finite counit $\varepsilon_{f,\mathcal O_E/\ell^n}$
([det-sp-tower-gluing]). Moreover $\gamma_{f,\mathcal O_E}(K)$ is
$R\varprojlim\gamma_{f,\bullet}(\operatorname{red}_YK)$, whose level $n$ is
$\gamma_{f,\mathcal O_E/\ell^n}(K_n)$ ([det-sp-tower-gamma], (2)). On normalized
towers $\operatorname{red}\circ R\varprojlim$ is isomorphic to the identity
([det-sp-normalized-equivalence]), and the towers involved are normalized
([det-sp-tower-gamma], (3)). Hence reducing modulo $\ell^n$ recovers the level-$n$
maps: the identification $(f^!_{\mathcal O_E}K)_n\simeq f^!_{\mathcal O_E/\ell^n}(K_n)$
obtained this way carries $\varepsilon_{f,\mathcal O_E}(K)_n\circ b_n^{-1}$ to the finite
counit. So it is the transpose $c_n(K)$, which is therefore an isomorphism, and it
carries $\gamma_{f,\mathcal O_E}(K)_n$ to $\gamma_{f,\mathcal O_E/\ell^n}(K_n)$. Here $b_n$
is the reduction of $\operatorname{red}_YRf_{!,\mathcal O_E}\simeq Rf_{!,\bullet}\operatorname{red}_X$
([det-sp-integral-direct-image-tower], (2)). Composing gives the trace identity.
For $A_{E,n}$, apply the finite comparisons $b,c$ along
$\mathcal O_E/\ell^m\to A_{E,n}$, which carry finite purity maps and counits to
finite purity maps and counits ([det-sp-reduction-compatibilities], (1) and (3)).

(2) Every object of $\Dbc(Y,E)$ has an integral model
([det-sp-rational-localized-hom]; [sk-lem-integral-models], (4), with
[sk-thm-sfb-rationalization-comparison]). By [det-sp-rational-adjunction], (1),
the counit of $Rf_{!,E}\dashv f^*_E(-)(d)[2d]$ is the scalar extension of the
integral counit transported along $\gamma_{f,\mathcal O_E}$, that is,
$(\operatorname{Tr}_{f,\mathcal O_E}(K_0)\otimes E)\circ b_E^{-1}$. By
[det-sp-rational-adjunction], (2), $\gamma_{f,E}$ is the counit-compatible
isomorphism with the Brown adjoint $f^!_E$, so this counit is also
$\varepsilon_{f,E}(K)\circ Rf_{!,E}(\gamma_{f,E}(K))=\operatorname{Tr}_{f,E}(K)$, which is
the trace identity. Applying $\varepsilon_{f,E}(K)\circ Rf_{!,E}(-)$ to both sides of
the first identity gives the same morphism: on the right by definition of
$\operatorname{Tr}_{f,E}$, on the left by the defining property of $c_E(K_0)$ and the
trace identity. Transposition under $Rf_{!,E}\dashv f^!_E$ is bijective, so the
first identity holds. In particular $c_E(K_0)$ is an isomorphism.

(3) For $E\subset F$ this is [det-sp-field-extension-towers], (2) and (3): the
comparisons are compatible with units, counits and purity maps, hence with the
traces. For $\Qlb$, [det-sp-qbar-adjunction] identifies the unit and counit
of $Rf_{!,\Qlb}\dashv f^*_{\Qlb}(-)(d)[2d]$ with the scalar extensions of those over
a finite $E$, and $\gamma_{f,\Qlb}$ is the counit-compatible comparison with the
Brown adjoint. The transposition argument of (2) then applies verbatim with
$-\otimes_E\Qlb$ in place of $-\otimes_{\mathcal O_E}E$.

The final assertion is the case $K=\Lambda_{\Spec k}$ of (1)–(3).
