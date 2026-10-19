+++
kind  = "proof"
of    = "lem-coef-integral-finite-extension"
+++
The $R$-module $S$ is finite free, so $\mathcal O_{L,X}=S\otimes_R\mathcal O_{E,X}$
is a finite free $\mathcal O_{E,X}$-module
([sk-prop-sfb-finite-extension-compatibility]); its tensor functor is
exact and commutes with derived inverse limits. In particular
$T_{S/R}$ preserves derived completeness, and no completion is needed. If $e$
is the ramification index, the ideals
$\pi_E^nS=\pi_L^{en}S$ are a cofinal system of powers of
the maximal ideal of $S$. The reductions of $T_{S/R}K$ along
this system are

$$
(S/\pi_E^nS)\otimes_{R/\pi_E^n}^LK_n,
\qquad K_n=K\otimes_R^L R/\pi_E^n.
$$

They are constructible and have a uniform Tor interval, since
[lem-coef-integral-residue-tor] supplies that interval for
$K_n$ and finite free extension preserves it. The normalized
tower reconstruction of [lem-coef-normalized-dvr-effectivity]
therefore gives an object of $D^b_c(X,S)$. The intervening
$\pi_L$-reductions are recovered by derived tensor from
any larger cofinal level, so they have the same Tor bound.

By [prop-coef-integral-dualizing], the reductions of the
integral dualizing objects are the finite dualizing objects.
At the cofinal levels [lem-coef-finite-free-extension] gives
the specified maps

$$
(S/\pi_E^nS)\otimes_{R/\pi_E^n}^L\omega_{X,R/\pi_E^n}
\xrightarrow{\sim}\omega_{X,S/\pi_E^nS}.
$$

Their quotient compatibility makes them a map of normalized
derived towers. Taking the derived limit, and using the
finite-free tensor comparison above, gives
$u_{L/E}$, including its naturality and compatibility with the
dualizing counit. This argument uses coherent maps of towers,
not just isomorphism classes of their terms.

The map $v_{K,M}$ is the transpose of scalar-extended
evaluation. To prove it is an isomorphism, forget the
$S$-action. Extension–restriction adjunction identifies its
target with
$R\mathcal Hom_R(K,S\otimes_RM)$. Locally choose a finite
free $R$-basis of $S$. Both this object and the source
identify with the corresponding finite sum of
$R\mathcal Hom_R(K,M)$, and $v_{K,M}$ becomes the identity
comparison of these sums. Forgetting coefficients is conservative,
so the comparison is an isomorphism. This reasoning uses finite
freeness of the coefficient extension, with no perfectness
assumption on $K$ on the whole space. All these internal Hom
objects are integral bounded constructible objects by
[cor-coef-integral-internal-hom].

Compose $v_{K,\omega_{X,R}}$ with internal Hom into
$u_{L/E}$ to obtain $\beta_{L/E,K}$. It identifies the
ambient integral duals of [thm-coef-integral-verdier].
Evaluation compatibility follows from the definition by
transposition. Transposing evaluation once more gives compatibility
with the double-dual map. For nested rings $R\subset S\subset U$,
the associator being used is

$$
U\otimes_S^L(S\otimes_R^LK)\xrightarrow{\sim}U\otimes_R^LK.
$$

For $u$, the unit and composition equations are the equations
of the finite comparisons, transported through derived inverse
limit. For $v$, both composites transpose to the
same evaluation after this associator; hence they are equal.
The same is true for $\beta$. These arguments also prove
compatibility with finite quotients and involve no chosen basis
in the definition of any comparison.
