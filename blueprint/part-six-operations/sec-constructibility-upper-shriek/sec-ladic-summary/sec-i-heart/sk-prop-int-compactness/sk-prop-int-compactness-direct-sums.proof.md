+++
kind = "proof"
of = "det-prop-int-compactness-direct-sums"
+++
(1) $Rp_*N\in\Dbc(Y,\mathcal O_E)$ by the integral case of
[sk-thm-sfb-proper-base-change]. On a weakly contractible affine $V\to Y$,
proper direct image of a torsion sheaf has cohomology in degrees $\le2d$
(Stacks, Tag 095U), and $\Gamma(V,-)$ is exact, so this bounds the cohomology of
sections. The reductions $N\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ are torsion
complexes in degrees $[-1,0]$, so their direct images have cohomology in
degrees $\le2d$. Direct image commutes with derived limits, so
$Rp_*N=R\varprojlim_nRp_*(N\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$ by derived
completeness of $N$, and one derived limit of a countable tower raises the
upper bound by at most one (Milnor sequence): $Rp_*N$ has cohomology in
degrees $\le2d+1$. It has no cohomology in negative degrees because $N$ is a
sheaf in degree $0$ and $p_*$ is left exact. For
$N=\varinjlim_iN_i$ with $N_i$ constructible, the family is bounded below
uniformly, so by continuity of direct image for bounded below systems
(as in [det-lem-int-ext](1)) $H^qRp_*N=\varinjlim_iH^qRp_*N_i$, a filtered
colimit of constructible sheaves, i.e. an object of $\IndCons(Y,\mathcal O_E)$,
vanishing outside $[0,2d+1]$.

(2) By (1), each cohomology object of $K$ contributes to $H^qRp_*K$ only from
degrees $[q-2d-1,q]$. The proofs of [sk-lem-proper-unbounded-window] and
[det-lem-proper-unbounded-window-ii], which use only this uniform bound, the
left completeness of the pro-étale derived category and the Milnor sequence,
show that $H^qRp_*K=H^qRp_*\tau_{[q-2d-1,q]}K$. On complexes with cohomology in
a finite range, $Rp_*$ commutes with direct sums by induction on the length of
the range, starting from the case of a single object of $\IndCons$, where it
follows from (1) and continuity. Truncations commute with direct sums, so
$Rp_*$ commutes with arbitrary direct sums in $\Dic(X,\mathcal O_E)$, with no
common lower bound needed.

(3) The objects of $\Loc(\Dbc(X,\mathcal O_E))$ whose direct image lies in
$\Loc(\Dbc(Y,\mathcal O_E))$ are closed under shifts and cones ($Rp_*$ is exact)
and under direct sums (by (2), since
$\Loc(\Dbc(X,\mathcal O_E))\subset\Dic(X,\mathcal O_E)$ by
[det-prop-int-compactness-compact](2)). They contain $\Dbc(X,\mathcal O_E)$ by
the first assertion of (1), extended to complexes by finite extensions.
Hence they form a localizing subcategory containing the generators, i.e. all
of $\Loc(\Dbc(X,\mathcal O_E))$; and $Rp_*$ preserves direct sums there by (2).
