+++
kind  = "proof"
of    = "det-cor-existence-ii-restriction"
+++
(1) $Rp_!$ is defined from a compactification $p=\bar p\circ j$ as $R\bar p_*\circ j_!$, and is
independent of the compactification up to canonical isomorphism
([sk-prop-sf-comp-coherence]). Since $p$ is proper, $X\xrightarrow{\mathrm{id}}X\xrightarrow{p}Y$
is a compactification, with $j=\mathrm{id}$ and $j_!=\mathrm{id}$. Hence $Rp_!\cong Rp_*$ on
$\Loc(\Dctf(X,\Lambda))$; in particular $Rp_*$ maps $\Loc(\Dctf(X,\Lambda))$ into
$\Loc(\Dctf(Y,\Lambda))$.

(2) By [sk-thm-existence] (2), $Rp_!\cong Rp_*$ maps $\Dctf(X,\Lambda)$ into
$\Dctf(Y,\Lambda)$; by (4), $p^!$ maps $\Dctf(Y,\Lambda)$ into $\Dctf(X,\Lambda)$. Both
$\Dctf$ categories are full subcategories of the localizing closures. So for
$K\in\Dctf(X,\Lambda)$ and $L\in\Dctf(Y,\Lambda)$ the adjunction bijection
$$
\Hom_{\Dctf(Y,\Lambda)}(Rp_*K,L)=\Hom_{\Loc}(Rp_!K,L)\cong\Hom_{\Loc}(K,p^!L)=\Hom_{\Dctf(X,\Lambda)}(K,p^!L)
$$
is natural in $K$ and $L$, i.e. the restriction of $p^!$ is right adjoint to the restriction
of $Rp_*$. Unit and counit are the restrictions of those on the localizing categories.
