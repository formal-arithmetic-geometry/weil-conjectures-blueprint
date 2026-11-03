+++
kind = "proof"
of = "det-sf-comp-coherence-single"
uses = ["sk-prop-proper-image-localizing", "sk-prop-ctf-finite-proper", "sk-thm-sfb-proper-base-change"]
+++
*Extension by zero.* By [sk-prop-proper-image-localizing], $j_!$ is exact,
preserves direct sums (it is a left adjoint, of $j^*$), carries
$\Dctf(X,\Lambda)$ into $\Dctf(\overline X,\Lambda)$ (constructibility by adding
the closed complement as a zero stratum, finite Tor amplitude stalkwise for
finite rings and via the local coefficient models for $\mathcal O_E$, $E$,
$\Qlb$), and therefore carries $\Loc(\Dctf(X,\Lambda))$ into
$\Loc(\Dctf(\overline X,\Lambda))$: the objects $K$ of
$\Loc(\Dctf(X,\Lambda))$ with $j_!K\in\Loc(\Dctf(\overline X,\Lambda))$ form a
triangulated subcategory (as $j_!$ is exact and the target is triangulated)
closed under direct sums (as $j_!$ preserves them and the target is closed
under them) containing $\Dctf(X,\Lambda)$, hence everything.

*Proper direct image.* By [sk-prop-proper-image-localizing], $Rp_*$ restricts
to an exact, direct-sum preserving functor
$\Loc(\Dctf(\overline X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$, and it carries
$\Dctf(\overline X,\Lambda)$ into $\Dctf(Y,\Lambda)$ by [sk-prop-ctf-finite-proper]
for finite $\Lambda$ and [sk-thm-sfb-proper-base-change] for
$\mathcal O_E$, $E$ and $\Qlb$ (where $\Dctf=\Dbc$).

*Composite.* A composite of exact functors preserving direct sums is exact
and preserves direct sums, and the composite carries $\Dctf(X,\Lambda)$ to
$\Dctf(Y,\Lambda)$ because each factor preserves $\Dctf$.
