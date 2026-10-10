+++
kind  = "proof"
of    = "sk-prop-av-mult-surjective"
uses = ["sk-cor-av-commutative", "sk-prop-av-mult-finite", "sk-prop-av-mult-hom"]
+++
The image $H:=[n](A)$ is a closed subgroup scheme of $A$: it is the
image of a homomorphism from the proper $A$ to the separated finite
type $A$, hence closed, and the group law, inverse and unit of $A$
restrict to it because $[n]\times[n]:A\times_kA\to H\times_kH$ is
surjective and $[n]$ is a homomorphism ([sk-prop-av-mult-hom]). Since $[n]$ is finite
([sk-prop-av-mult-finite]) its fibres are zero-dimensional, so the
dimension formula for a surjective morphism of varieties of finite
type over a field gives
$\dim H=\dim A-\dim A[n]=\dim A$. Now $A$ is irreducible
([sk-prop-av-char]) and $H\subseteq A$ is closed of full dimension,
so $H_{\mathrm{red}}=A$ and hence $H=A$.
