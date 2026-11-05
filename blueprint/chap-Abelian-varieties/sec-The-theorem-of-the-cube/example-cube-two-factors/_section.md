+++
id = "example-cube-two-factors"
kind = "example"
title = "Two factors do not suffice"
order = 1474
uses = ["lemma-triviality-fibres"]
+++
Let $E$ be an elliptic curve over an algebraically closed field, with
origin $O$, and let $\Delta\subset E\times E$ be the diagonal. On
$E\times E$ put

$$
\mathcal L=\mathcal O_{E\times E}\bigl(\Delta-E\times\{O\}-\{O\}\times E\bigr).
$$

Consider the slice $E\times\{t\}$. It meets the diagonal in the point
$t$, and the divisor $\{O\}\times E$ meets it in the point $O$. The divisor $E\times\{O\}$, on the other hand, is pulled back from the second factor, so it
contributes the trivial sheaf for every $t$. Hence the restriction is
$\mathcal O_E(t-O)$. By symmetry the restriction to $\{t\}\times E$ is
also $\mathcal O_E(t-O)$. In particular $\mathcal L$ is trivial on both
slices through $(O,O)$.

However, $\mathcal L$ is not trivial, because for $t\neq O$ the sheaf
$\mathcal O_E(t-O)$ is nontrivial. Indeed, a rational function with
divisor $t-O$ would be a map $E\to\mathbf P^1$ of degree one, which is
impossible in genus one. The set of $t$ over which the fibre is trivial
is the point $O$. It is closed, as Lemma [lemma-triviality-fibres]
below predicts, but not open.
