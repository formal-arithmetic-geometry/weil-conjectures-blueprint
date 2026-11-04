+++
kind = "proof"
of = "proposition-dctf-x-qbar-2-colimit"
order = 643
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "lemma-inverse-image-coefficient-sheaves", "definition-lisse-sheaves", "lemma-acyclic-resolutions", "lemma-proper-direct-image-unbounded-complexes", "lemma-extension-scalars-preserves-dctf"]
+++
An equivalence with a $2$-colimit amounts to two statements, essential
surjectivity on objects and a bijection on morphisms. Both are parts of
Lemma [lemma-descent-finite-coefficient-field], and we recall how each
is proved before putting them together.

The statement about objects is
Lemma [lemma-descent-finite-coefficient-field](2). Its proof first descends the
lisse sheaves on the strata, together with their transition matrices. It
then descends the connecting morphisms of a finite Postnikov tower, and in
this way the complexes themselves descend. The bijection
on morphisms is Lemma [lemma-descent-finite-coefficient-field](1) with
$r=0$, since $D^b_{\mathrm{ctf}}$ is a full subcategory. Its proof uses the continuity of
Ext out of a constructible complex
(Lemma [lemma-continuity-ext-out-constructible-complex]), applied to the filtered
colimit $\QbarX=\varinjlim_F F_X$. Surjectivity says that
every morphism descends to a finite stage, and injectivity says that two
morphisms with the same image agree at a later finite stage. Now consider the
category whose objects are the pairs $(E,K)$ with $K\in D^b_{\mathrm{ctf}}(X,E)$ and whose
Hom sets are these colimits. Together with descent of objects, the statements
above say exactly that the functor from this category to $D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)$ is
fully faithful and essentially surjective.
