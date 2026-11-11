+++
kind = "proof"
of = "corollary-curve-preserving-geometric-irreducibility"
order = 1334
uses = ["proposition-etale-implications", "theorem-pro-etale-refinements-weakly-etale", "proposition-sp-unique-adjoint", "lemma-curve-preserving-finite-cover", "definition-compactification-refinement"]
+++
We translate irreducibility into the surjectivity of $\pi_1(C)$ onto
one finite group, and then find $C$ with Bertini's theorem applied to
the corresponding cover.

Choose a finite extension $E$ of $\mathbf Q_\ell$ over which all the sheaves are
defined, and apply Lemma [lemma-detecting-irreducibility-finite-quotient] to their geometric
representations. Let $T\to X$ be the connected Galois cover
corresponding to the intersection of the kernels of the resulting
finite quotients of $\pi_1(X)$, and let $Q$ be its group. In dimension
one, we take $C=X$. Otherwise $\dim X\ge2$, and we apply
Lemma [lemma-curve-preserving-finite-cover] to $T$ and the given
points. If no points are given we add one, since the lemma needs $S$
nonempty. As $T\times_XC$ is connected, $\pi_1(C)$ acts transitively on
the fibre of the $Q$-torsor $T\times_XC\to C$, so its image in $Q$ is
all of $Q$. Each of the finite quotients above is a quotient of $Q$.
Hence $\pi_1(C)$ has the same image as $\pi_1(X)$ in each of them, and
Lemma [lemma-detecting-irreducibility-finite-quotient], applied with $\Pi=\pi_1(X)$ and
$\Pi'$ the image of $\pi_1(C)$, shows that the restrictions remain
geometrically irreducible. By
Lemma [lemma-curve-preserving-finite-cover] the curve and the points
are defined over a finite extension of the constant field. The curve
$C$ is geometrically connected because it is connected over
$\overline{\mathbf F}_q$.
