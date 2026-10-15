+++
kind  = "proof"
of    = "lem-exc-proetale-closed-support"
+++
Use the exact fully faithful closed direct image and its identification
with module sheaves supported on $Z$, now proved in
[lem-exc-proetale-closed-exact], [lem-exc-proetale-closed-fully-faithful], [lem-exc-proetale-closed-essential-image].
These results concern all module sheaves. Their hypotheses
hold here: in a Noetherian scheme every open subset is
quasi-compact, and this remains true on each affine open, so
the complementary open immersion is quasi-compact.
Write $i^!=i^!_0$ for the sheaf functor of
[def-exc-proetale-sections-with-support].
The kernel restricts to zero on $U$, hence lies in the image of
$i_*$. Every map $i_*M\to N$ has image in this kernel, because
$j^*i_*M=0$. Full faithfulness of $i_*$ gives
$\operatorname{Hom}(i_*M,N)=\operatorname{Hom}(M,i^!N)$.

Choose a K-injective complex $I$ with injective terms resolving
$K$, by [prop-weil-pbc-kinjective-resolutions-exist].
Since $i_*$ and the $j_!$ of [prop-exc-open-adjoint] are
exact, the adjunction shows that $i^!I$ and $j^*I$ are
K-injective, so the right derived functor of the sheaf-level $i^!$
exists and is computed on such resolutions.
Complex-level adjunction then gives $i_*\dashv Ri^!$ on the
ambient categories. If a Brown right adjoint to $Ri_*=i_*$ has
also been chosen, uniqueness of right adjoints identifies it with
this functor, including the counit.
