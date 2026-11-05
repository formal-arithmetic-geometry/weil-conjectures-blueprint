+++
kind = "proof"
of = "proposition-no-fixed-class-degree-one--1"
order = 1097002
uses = ["lemma-proper-smooth-model", "proposition-kummer-duality-integral-tate-module", "proposition-jacobian-over-ground-field", "proposition-multiplication-n", "proposition-no-frobenius-fixed-vector"]
+++
Choose a smooth proper geometrically connected compactification
$j_0:U_0\hookrightarrow C_0$ by Lemma [lemma-proper-smooth-model],
and write $j:U\hookrightarrow C$ for its geometric fibre.

*Extension across the boundary.* Fix a boundary point $z$ and choose
a positive power of Frobenius fixing it, with $Q=q^m$. Local monodromy
of a Frobenius-fixed $A_r$-torsor at $z$ is killed by $Q-1$.
Consequently there is an integer $v\geq0$, independent of $r$, such
that $\ell^v$ kills this local monodromy. This is
`AlgebraicGeometry.Scheme.EtaleTorsor.exists_pow_mul_monodromy_eq_zero`.
Apply it at level $n+v$. An element of $\mathbf Z/\ell^{n+v}$ killed
by $\ell^v$ reduces to zero modulo $\ell^n$, so compatibility forces
the local monodromy of $T_n$ at $z$ to vanish.

The kernels of the maps $\pi_1(U)\to\pi_1(U\cup\{z\})$, as $z$
runs through the finite boundary, generate the kernel of
$\pi_1(U)\to\pi_1(C)$ as a closed subgroup. Hence the characters
$\rho_n$ factor through $\pi_1(C)$, giving torsors $T'_n$ on $C$
whose restrictions are isomorphic to $T_n$. The map
$\pi_1(U)\to\pi_1(C)$ is surjective, so compatibility and
Frobenius invariance can be checked after restriction to $U$.
This gives a compatible Frobenius-fixed system on $C$
(`AlgebraicGeometry.Scheme.EtaleTorsor.exists_extension_of_isIsomorphic_mapIso`).

*The proper case.* Let $J_0$ be the Jacobian over $k_0$, as in
Proposition [proposition-jacobian-over-ground-field]. The finite-level
pairings of Proposition [proposition-kummer-duality-integral-tate-module]
associate to $T'_n$ a character

$$
\psi_n:J_0(k)[\ell^n]\longrightarrow\mathbf Z/\ell^n.
$$

These characters are Frobenius-invariant and satisfy
$\psi_n(\ell y)=\psi_{n+1}(y)\bmod\ell^n$. A zero character
implies that the corresponding torsor has a section.
By Proposition [proposition-multiplication-n], $J_0(k)$ is
$\ell$-divisible and its $\ell^n$-torsion is finite. The finiteness
argument in Proposition [proposition-no-frobenius-fixed-vector] shows
that Frobenius has only finitely many fixed points on $J_0(k)$,
namely $J_0(k_0)$.

The finite-group argument
`AddSubgroup.eq_zero_of_forall_map_eq_of_finite_fixedPoints` now
applies. Indeed, the kernels of $F-1$ on $J_0(k)[\ell^r]$ have
uniformly bounded order. Thus a fixed power $\ell^N$ sends each
of these finite groups into the image of $F-1$, which every
$\psi_r$ kills. Given $y\in J_0(k)[\ell^n]$, divisibility gives
$y=\ell^N z$ with $z\in J_0(k)[\ell^{n+N}]$. The value
$\psi_{n+N}(z)$ is killed by $\ell^N$, so its reduction modulo
$\ell^n$ is zero; compatibility identifies that reduction with
$\psi_n(y)$. Therefore all $\psi_n$ vanish and every $T'_n$ has a
section. This is
`AlgebraicGeometry.Scheme.EtaleTorsor.exists_section_of_isIsomorphic_mapIso_of_isProper`.

Finally, restrict a section of $T'_n$ to $U$ and compose with the
isomorphism $j^*T'_n\simeq T_n$ to obtain the required section.
