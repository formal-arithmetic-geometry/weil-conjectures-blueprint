+++
kind = "proof"
of = "lemma-detecting-irreducibility-finite-quotient"
order = 1328
+++
Recall Burnside's theorem: an algebra of endomorphisms of a
finite-dimensional vector space over an algebraically closed field that
acts irreducibly is the full endomorphism algebra. Absolute
irreducibility thus means that the group spans the full matrix algebra. We
detect spanning by a nonzero determinant of $n^2$ group elements. Such
a determinant stays nonzero when we change the elements by a congruence
modulo a high power of $\pi_E$.

The compact group $\rho(\Pi)$ stabilizes a lattice $L$. Indeed, the
stabilizer of any lattice $L_0$ is open, hence of finite index in
$\rho(\Pi)$. So $L_0$ has only finitely many translates, and their sum
is a $\rho(\Pi)$-stable lattice. By absolute irreducibility and
Burnside's theorem, there are elements $g_1,\ldots,g_{n^2}$ whose
matrices span $\operatorname{End}_E(V)$. In a basis of $L$, the
determinant $\Delta$ of their matrices, written as column vectors, is
nonzero and integral. Choose $N>v_{\pi_E}(\Delta)$. Suppose that
$g'_1,\ldots,g'_{n^2}$ have matrices congruent to those of the $g_i$
modulo $\pi_E^N$. Since the determinant is a polynomial with integer
coefficients in the entries, their determinant $\Delta'$ satisfies
$\Delta'\equiv\Delta\pmod{\pi_E^N}$. Hence
$v_{\pi_E}(\Delta')=v_{\pi_E}(\Delta)$, and in particular
$\Delta'\ne0$. A subgroup as in the statement contains such elements.
Its matrices therefore span the whole matrix algebra, also after any
field extension, and by Burnside's theorem it acts absolutely
irreducibly. Finally, the image of $\Pi$ in $\GL(L/\pi_E^NL)$ is a
finite quotient of $\Pi$, since by continuity the kernel is open.
