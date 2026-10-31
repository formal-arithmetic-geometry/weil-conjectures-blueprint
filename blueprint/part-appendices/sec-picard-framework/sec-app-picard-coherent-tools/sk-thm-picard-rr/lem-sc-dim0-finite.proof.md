+++
kind  = "proof"
of    = "lem-sc-dim0-finite"
+++
(The underlying space of a scheme of finite type over a field is
Noetherian, by Hilbert's basis theorem on an affine cover, and $T_0$, as
is every scheme.)

First, every point $z\in Z$ is closed in $Z$. Let $y$ lie in the
closure of $\{z\}$ in $Z$. The closures of $\{y\}$ and $\{z\}$ in $Z$
are irreducible closed subsets of $Z$ with
$\overline{\{y\}}\subseteq\overline{\{z\}}$. A strict inclusion would be
a chain of irreducible closed subsets of length one, contradicting
$\dim Z\le0$, so $\overline{\{y\}}=\overline{\{z\}}$. The points $y$ and
$z$ then have the same closure, hence are equal since $X$ is $T_0$. Thus
$\{z\}$ is closed in $Z$, hence in $X$ because $Z$ is closed.

Next, every irreducible component of $Z$ is a single point: if $C$ is an
irreducible component containing $z$, then $\{z\}\subseteq C$ is an
inclusion of irreducible closed subsets of $Z$, hence an equality by
$\dim Z\le0$ as above. The subspace $Z$ of the Noetherian space $X$ is
Noetherian, so it has finitely many irreducible components, and every
point lies in one of them. Hence $Z$ is finite.
