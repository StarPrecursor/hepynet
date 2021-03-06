DEFAULT_CFG = {
    "config": {"include": [],},
    "job": {
        "job_name": "JOB_NAME_DEF",
        "job_type": "JOB_TYPE_DEF",
        "save_dir": ".",
        "load_job_name": "LOAD_JOB_NAME_DEF",
        "fix_rdm_seed": True,
        "rdm_seed": 1024,
    },
    "input": {
        "input_path": "",
        "reshape_input": True,
        "reweight_input": True,
        "negative_weight_process": "to_zero",  # could also be "to_positive" or "keep"
        "feature_norm_alias": {},
        "sig_sumofweight": 1000,
        "bkg_sumofweight": 1000,
        "data_sumofweight": 1000,
        "reset_feature": False,
        "reset_feature_name": "RESET_FEATURE_NAME_DEF",
        "rm_negative_weight_events": False,
        "arr_path": "",
        "arr_version": "",
        "variation": "",
        "channel": "",
        "campaign": "",
        "region": "",
        "channel": "",
        "sig_key": "all",
        "sig_list": [],
        "bkg_key": "all",
        "bkg_list": [],
        "data_key": "all",
        "data_list": [],
        "selected_features": [],
        "validation_features": [],
        "cut_features": [],
        "cut_values": [],
        "cut_types": [],
        "cut_expression": None,
        "test_rate": 0.2,
    },
    "train": {
        "model_name": "MODEL_NAME_DEF",
        "model_class": "Model_Sequential_Flat",
        "output_bkg_node_names": [],
        "layers": 1,
        "nodes": 1,
        "learn_rate": 0.01,
        "learn_rate_decay": 0.01,
        "batch_size": 32,
        "epochs": 1,
        "momentum": 0,
        "nesterov": False,
        "dropout_rate": 0,
        "sig_class_weight": 1,
        "bkg_class_weight": 1,
        "val_split": 0.25,
        "k_folds": None,
        "use_early_stop": False,
        "early_stop_paras": {
            "monitor": "val_loss",
            "min_delta": 0,
            "patience": 1,
            "mode": "min",
            "restore_best_weights": True,
        },
        "train_metrics": [],
        "train_metrics_weighted": ["accuracy"],
        "save_model": True,
        "verbose": 0,
    },
    "apply": {
        "color_cycle": [
            "#f99157",  # orange
            "#5fb3b3",  # cyan
            "#ec5f67",  # red
            "#6699cc",  # blue
            "#fac863",  # yellow
            "#99c794",  # green
            "#c594c5",  # pink
            "#ab7967",  # brown
            "#cdd3de",  # grey
            "#343d46",  # black
        ],
        "plot_atlas_label": False,
        "atlas_label": {},
        "check_model_epoch": False,
        "epoch_check_interval": 5,
        "book_history": False,
        "cfg_history": {},
        "book_kine": False,
        "cfg_kine": {
            "separate_bkg_sig": True,
            "bkg_scale_raw": 1,
            "bkg_scale_processed": 1,
            "sig_scale_raw": 1,
            "sig_scale_processed": 1,
            "hist_kwargs_sig": {  # kwargs of plt.hist
                "bins": 40,
                "logbin": False,
                "logx": False,
                "logy": False,
                "histtype": "step",
                "density": False,
                "facecolor": "#f99157",  # orange
                "edgecolor": "#f99157",
                "lw": 2,
            },
            "hist_kwargs_bkg": {
                "bins": 40,
                "logbin": False,
                "logx": False,
                "logy": False,
                "histtype": "stepfilled",
                "density": False,
                "facecolor": "#5fb3b3",  # cyan
                "edgecolor": "#5fb3b3",
            },
            "save_format": "png",
            "x_label": "",
            "y_label": "",
            # dedicated feature configs can be made like the following:
            ## feature:
            ##   bins: 25
            ##   range: [10, 200]
            # feature config will overwrite common plot configs
        },
        "book_cor_matrix": False,
        # model dependent studies
        "jump_model_studies": False,
        "book_fit_npy": False,
        "cfg_fit_npy": {
            "fit_npy_region": "",
            "fit_npy_branches": [],
            "npy_save_dir": "",
        },
        "book_confusion_matrix": False,
        "cfg_confusion_matrix": {"dnn_cut": 0.5},
        "book_roc": False,
        "book_pr": False,
        "book_train_test_compare": False,
        "cfg_train_test_compare": {
            "sig_key": None,
            "bkg_key": None,
            "plot_title": "train/test MVA scores compare",
            "bkg_color": "#f99157",  # orange
            "sig_color": "#5fb3b3",  # cyan
            "bins": 25,
            "range": [0, 1],
            "density": False,
            "log": False,
            "logy_min": 0.001,
            "save_format": "png",
        },
        "book_mva_scores_data_mc": False,
        "cfg_mva_scores_data_mc": {
            "sig_list": [],
            "bkg_list": [],
            "apply_data": False,
            "data_key": "",
            "apply_data_range": None,
            "plot_title": "MVA scores",
            "bkg_color": "#f99157",  # orange
            "sig_color": "#5fb3b3",  # cyan
            "bins": 25,
            "range": [0, 1],
            "density": False,
            "log": False,
            "logy_min": 0.001,
            "save_format": "png",
            "use_root": False,
        },
        "book_significance_scan": False,
        "cfg_significance_scan": {"significance_algo": "s_sqrt_b_rel",},
        "book_cut_kine_study": False,
        "cfg_cut_kine_study": {
            "separate_sig_bkg": False,
            "save_ratio_table": False,
            "bins": 40,
            "range": None,
            "histtype": "stepfilled",
            "alpha": 0.3,
            "density": False,
            "bkg_color": "#f99157",  # orange
            "sig_color": "#5fb3b3",  # cyan
            "dnn_cut_list": None,
            "save_format": "png",
        },
        "book_importance_study": False,
        "cfg_importance_study": {"log": False},
    },
    "para_scan": {"perform_para_scan": False,},
    "run": {
        "datestr": "",
        "npy_path": "",
        "config_collected": False,
        "input_dim": None,
    },
}
