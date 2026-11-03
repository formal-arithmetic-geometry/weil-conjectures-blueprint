# Titles for the declarations the tex leaves unnamed, keyed by label.
GENERATED_TITLES = {
    'proposition-etale-implications': 'Étale, ind-étale and weakly étale ring maps',
    # Constructible complexes
    'proposition-ctf-equals-bc': 'Constructible complexes have finite Tor amplitude for $\\ell$-adic coefficients',
    'corollary-coefficient-heart-b': 'Generators of $D^b_c$ with field coefficients',
    # Proper base change
    'remark-cohomology-modules-underlying-abelian': 'Cohomology of modules and of abelian sheaves',
    'remark-henselian-pairs-facts': 'Facts on henselian pairs',
    'remark-finiteness-small-etale-topoi': 'Finiteness facts for étale sheaves on the projective line',
    # Construction of f^!
    'corollary-ind-heart-b': 'Ext from a constructible sheaf into ind-constructible sheaves',
    'corollary-ambient-ind-derived': 'The derived category of ind-constructible sheaves',
    # Constructibility of f^!
    'example-closed-support': 'Local cohomology at the origin of the affine line',
    # Smooth purity
    'proposition-sp-unique-adjoint': 'Uniqueness of the right adjoint of $Rf_!$',
    'definition-sp-scalar-extension': 'Extension of scalars',
    'lemma-sp-reduction': 'Extension of scalars commutes with $Rf_!$ and $f^!$',
    'proposition-sp-integral-towers': 'Integral constructible complexes as towers',
    'lemma-sp-tower-adjunction-foundation': 'Reduction to towers is left adjoint to the derived limit',
    'proposition-sp-tower-geometric': 'The adjunction $Rf_!\\dashv f^!$ on constructible towers',
    'proposition-sp-integral-adjunction': 'The integral right adjoint built from towers',
    'proposition-sp-rational': 'Smooth purity with coefficients in $E$',
    'theorem-sp-qbar': 'Smooth purity with coefficients in $\\overline{\\mathbf Q}_\\ell$',
    # The trace formula
    'remark-locality-warning': 'Local terms are not computed stalk by stalk',
    # Weights
    'definition-weights': 'Weights, purity and mixedness',
    # Proof of the Weil conjectures
    'definition-reciprocal-root': 'Reciprocal roots',
}

# Declarations with no label: (start of the statement) -> (id, title).  The
# title is used only when the tex gives none.
UNLABELLED = {
    'Let $U$ be an object of $X_{\\proet}$.\n\\begin{enumerate}':
        ('proposition-pro-etale-coverings', 'Coverings in the pro-étale site'),
    '\\leavevmode\n\\begin{enumerate}\n\\item If $T$ is a w-local spectral space':
        ('proposition-w-local-components', 'Connected components of w-local spaces and rings'),
    'Let $U$ be an object of $X_{\\proet}$ and $f:X\\to Y$ a morphism of':
        ('proposition-unbounded-functors-products', 'Unbounded derived functors preserve products and limits'),
    # Constructible complexes
    '\\leavevmode\n\\begin{enumerate}\n\\item For Noetherian $X$, every locally closed subset':
        ('remark-constructible-sheaves-coefficient-rings', 'Constructible sheaves for the individual coefficient rings'),
    # Proper base change
    'For $f$ proper and $F$ a torsion sheaf on $X$, is the stalk':
        ('question-stalks-proper-direct-image', 'Stalks of higher direct images along a proper map'),
    'Properness in $(C_7)$ is needed':
        ('remark-properness-needed-c7', 'Why properness is needed in $(C_7)$'),
    # Construction of f^!
    '\\leavevmode\n\\begin{enumerate}\n\\item By Nagata':
        ('remark-compactifications', None),
    # Constructibility of f^!
    'We use the open immersion $j_\\infty':
        ('example-compact-supports-running-example', None),
    # Smooth purity
    '\\leavevmode\n\\begin{enumerate}\n\\item For the projection $\\mathbf A^d_Y\\to Y$':
        ('remark-trace-map-special-cases', 'The trace map in two special cases'),
    # The trace formula
    'Does the Lefschetz formula hold for Frobenius?':
        ('question-lefschetz-formula-frobenius', 'The Lefschetz formula for Frobenius'),
    'In Lemma~\\ref{lemma-integral-models-rational-frobenius-correspondences}, $K_0$ need not':
        ('remark-integral-frobenius-correspondences-not-invertible', None),
    'The functional equation is an\nidentity of rational functions':
        ('remark-duality-and-weights', None),
    # Purity of real sheaves
    'Let $\\mathcal V$ be a nonzero lisse Weil sheaf of rank $r$ on a smooth':
        ('remark-determinant-weight-pure-constituents', 'Determinant weight of a sheaf with pure constituents'),
    # Proof of the Weil conjectures
    'We have $\\#\\mathbf P^d(\\mathbf F_{q^m})=1+q^m':
        ('example-zeta-projective-space-elliptic-curve', 'Projective space and elliptic curves'),
    # Nagata compactification and Chow's lemma
    'The same proof works for qcqs $\\overline X$ whenever':
        ('remark-non-noetherian-compactifications', 'Non-Noetherian compactifications'),
}
