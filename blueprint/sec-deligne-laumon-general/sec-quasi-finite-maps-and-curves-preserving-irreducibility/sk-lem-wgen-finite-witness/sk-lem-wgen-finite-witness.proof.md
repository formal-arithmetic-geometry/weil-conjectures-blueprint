+++
kind = "proof"
of = "sk-lem-wgen-finite-witness"
+++
By Burnside's theorem, absolute irreducibility means
that the group spans the full matrix algebra, and this is detected by
a nonzero determinant, hence by a congruence modulo a power of
$\pi_E$. Recall Burnside's theorem: an algebra of endomorphisms of a
finite-dimensional vector space over an algebraically closed field that
acts irreducibly is the full endomorphism algebra.

The compact group $\rho(\Pi)$ stabilizes a lattice $L$. Indeed, the
stabilizer of any lattice $L_0$ is open, hence of finite index in
$\rho(\Pi)$, so $L_0$ has only finitely many translates, and their sum
is a $\rho(\Pi)$-stable lattice. By absolute irreducibility and
Burnside's theorem, there are elements $g_1,\ldots,g_{n^2}$ whose
matrices span $\operatorname{End}_E(V)$. In a basis of $L$, the
determinant $\Delta$ of their matrices, written as column vectors, is
nonzero and integral. Choose $N>v_{\pi_E}(\Delta)$. If
$g'_1,\ldots,g'_{n^2}$ have matrices congruent to those of the $g_i$
modulo $\pi_E^N$, then their determinant $\Delta'$ satisfies
$\Delta'\equiv\Delta\pmod{\pi_E^N}$, because the determinant is a
polynomial with integer coefficients in the entries. Hence
$v_{\pi_E}(\Delta')=v_{\pi_E}(\Delta)$, and in particular
$\Delta'\ne0$. A subgroup as in the statement contains such elements,
and therefore its matrices span the whole matrix algebra, also after
any field extension. By Burnside's theorem it acts absolutely
irreducibly. Finally, by continuity the kernel of
$\Pi\to\GL(L/\pi_E^NL)$ is open, so the image of $\Pi$
is a finite quotient of $\Pi$.
