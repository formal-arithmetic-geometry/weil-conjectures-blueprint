+++
kind  = "proof"
of    = "lem-weil-pbc-w-local-partition"
+++
We recall explicitly the affine component fact being used. The intersection
of all clopen neighbourhoods of a point is its connected component. Indeed
this intersection is the spectrum of the localization obtained by inverting
all idempotents equal to one at the point. A nontrivial idempotent in that
localization would descend, together with its idempotent equation, to a
finite stage, and then give a smaller clopen neighbourhood. Thus its spectrum
is connected. In the w-local case each component contains exactly one closed
point [det-pe-wlocal-components].

Write $X^c=V(J)$. The ring $A/J$ has all primes maximal. Its spectrum is
compact Hausdorff with a basis of clopen sets: after quotienting by its
nilradical, every localization at a prime is a field, so for each $a$ the
ideals $(a)$ and its annihilator generate the unit ideal; this produces an
idempotent with the same basic open as $a$. This proves the assertion about
profiniteness. Distinct closed points belong to distinct components, hence
are separated by clopen subsets of $X$, by the component fact. If $E\subset
X^c$ is clopen, compactness first separates each point of $E$ from all of
$X^c\setminus E$ by finitely many clopen subsets of $X$, and then covers $E$
by finitely many such subsets. Their union extends $E$. It is unique, because
every nonempty clopen subset contains a closed point. Finally an open set is
stable under generalization, so it contains the whole component of each
closed point it contains.
