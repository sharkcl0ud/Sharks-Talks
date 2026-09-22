init -990 python in mas_submod_utils:
    Submod(
        author="sharkcl0ud",
        name="Shark Talk",
        description="Adds few topics about those badass creatures!!",
        version="1.0.0",
        settings_pane=None,
        version_updates={}
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Shark Talk",
            user_name="sharkcl0ud",
            repository_name="Shark-Talk"
        )