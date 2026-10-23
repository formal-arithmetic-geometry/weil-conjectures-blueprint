+++
kind  = "proof"
of    = "thm-weil-pbc-stein-inputs"
uses = ["def-weil-pbc-stein-factorization", "def-weil-pbc-henselian-terminology"]
+++
*(i)* For $A$ Noetherian and $p$ proper, $p_*\mathcal O_Y$ is a coherent
$\mathcal O_S$-module (Stacks Project, Tag 02O5), so its global sections $B$
form a finite $A$-module.

*(ii) Nonemptiness.* The image $p(C)$ is closed and nonempty, so it contains a
closed point of $S$, a maximal ideal; it contains $I$, because $I$ lies in the
Jacobson radical of $A$ for a henselian pair. So $C\cap Y_0\neq\emptyset$.

*(ii) Connectedness.* Give $C$ its reduced induced closed subscheme structure
$Z$; then $g:Z\to S$ is proper, $Z\cong C$ is irreducible, hence connected, and
$Z_0=Z\times_SV(I)$ is nonempty with image $C\cap Y_0$ in $Y$. Let
$Z\xrightarrow{q}\operatorname{Spec}B\to S$ be the Stein factorization of $g$,
$B=\Gamma(Z,\mathcal O_Z)$ [def-weil-pbc-stein-factorization]. For proper $g$
over an affine base (Stacks Project, Tag 03H2), $A\to B$ is integral, and $q$
is proper and surjective with connected fibres.

Since $B$ is integral over $A$, the pair $(B,IB)$ is henselian
[def-weil-pbc-henselian-terminology]: $IB$ lies in the Jacobson radical, and
idempotents of $B/IB$ lift uniquely to $B$, because every finite subset of $B$
lies in a finite $A$-subalgebra, over which idempotents lift uniquely. As $Z$
is connected, $B\neq0$ has no idempotents other than $0$ and $1$, so neither
has $B/IB$, which is nonzero because $IB$ lies in the Jacobson radical of
$B\neq0$. Hence $V(IB)\subseteq\operatorname{Spec}B$ is nonempty and connected.

Finally $q$ is closed and surjective, hence a quotient map, with connected
fibres, so the preimage $q^{-1}(V(IB))$ of the closed connected set $V(IB)$ is
connected. This preimage is $g^{-1}(V(I))$, the image of $Z_0$ in $Z$, because
the preimage of $V(I)$ under $\operatorname{Spec}B\to S$ is $V(IB)$. Its image
$C\cap Y_0$ in $Y$ is therefore connected.
