+++
kind  = "proof"
of    = "lem-sc-generic-kummer-residues"
+++
Kummer's polynomial construction in [def-sc-kummer-sequence]
gives $H^1(E,\mu_n)=E^\times/E^{\times n}$ for any field $E$;
the next term $H^1(E,\mathbf G_m)$ is zero by Hilbert 90 ([cor-sc-hilbert-90-field]).
On a quasi-compact etale curve $V\to C$, its generic fibre is
a finite disjoint union of fields. Take the valuations of a
representing rational function at the closed points of $V$.
Only finitely many valuations are nonzero, so these maps land
in the direct sum. They commute with etale restriction: an
etale extension of discrete valuation rings has ramification
index one. They therefore define the displayed map after
sheafification of the cohomology presheaf.

At a geometric closed point the stalk formula
[prop-weil-pbc-strict-henselization-stalk-formula]
identifies the map with

$$
E^\times/E^{\times n}\longrightarrow\mathbf Z/n,
\qquad a\longmapsto v(a)\bmod n,
$$

where $E$ is the fraction field of the strict local ring $R$.
This is a discrete valuation ring by
[lem-sc-smooth-regular], [lem-sc-regular-dim1-dvr].
Every unit of $R$ has an $n$-th root: choose a root in its
separably closed residue field and lift it by Hensel's lemma,
since the derivative is a unit. A uniformizer has valuation one.
Thus the stalk map is bijective. Both generic stalks are zero.
The isomorphism follows from
[prop-weil-pbc-geometric-stalks-exact].
