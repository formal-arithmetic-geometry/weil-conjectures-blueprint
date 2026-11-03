+++
kind = "proof"
of = "det-pd-dualizing-complex-ctf"
uses = ["det-existence-restriction", "lem-sf-mate"]
+++
On the point $s$ the constant sheaf $\Lambda_s$ is constructible, and its
Tor amplitude is $[0,0]$; for integral and rational $\Lambda$ the category
$\Dctf(s,\Lambda)$ is $\Dbc(s,\Lambda)$, which contains $\Lambda_s$. So
$\Lambda_s\in\Dctf(s,\Lambda)$. The structure morphism $a_X$ is separated of
finite type, so the exceptional inverse image $a_X^!$ sends
$\Dctf(s,\Lambda)$ into $\Dctf(X,\Lambda)$ by [det-existence-restriction].
Hence $\omega_{X,\Lambda}=a_X^!\Lambda_s\in\Dctf(X,\Lambda)$.

For $f\colon X\to Y$ one has $a_X=a_Y\circ f$, and the composition
isomorphism $(a_Y\circ f)^!\simeq f^!a_Y^!$ of [lem-sf-mate], applied to
$\Lambda_s$, gives $\omega_{X,\Lambda}\simeq f^!\omega_{Y,\Lambda}$.
