+++
kind = "proof"
of = "proposition-comparison-immersions--3"
order = 139007
uses = ["proposition-comparison-morphism-inverse-image", "proposition-topos-functoriality", "theorem-comparison-direct-images"]
+++
The direct images commute with restriction to the étale subsite:
$\nu_{X,*}g_{\mathrm{pro}\acute{e}t,*}\simeq
g_{\acute{e}t,*}\nu_{Y,*}$. Taking the conjugate under the composite
inverse-image/direct-image adjunctions gives
$g_{\mathrm{pro}\acute{e}t}^*\nu_X^*\simeq\nu_Y^*g_{\acute{e}t}^*$
on sheaves. All these inverse-image functors are exact. Apply the
sheaf isomorphism termwise to complexes, pass to derived categories,
and use the comparison between the derived functor of a composite
of exact functors and the composite of their derived functors.

For the final direct-image assertion, a closed immersion is
quasi-compact and quasi-separated, so
[theorem-comparison-direct-images] applies.
